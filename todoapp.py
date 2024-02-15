from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData, create_engine
import os


file_path = os.path.join(os.path.abspath(os.getcwd()), 'temp', 'todo2.db')
print(file_path)

# engine = create_engine("sqlite:///todo2.db")
# metadata_obj = MetaData()


app = Flask(__name__)

# Ustalamy gdzie będzie nasza baza danych. Robimy to przez app.config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + file_path

# SQLAlchemy sam sobie wyciągnie ścieżkę i konektor z app
db = SQLAlchemy(app)


'''Tworzymy model, który będzie reprezentowała table w bazie danych.
    Pola w tej klasie reprezentują kolumny w odpowiedniej tabeli.
     db.Model specjalna klasa od SQLAlchemy'''


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}


@app.route("/", methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = Task(name=request.form["task"])
        db.session.add(task)
        db.session.commit()

    tasks = Task.query.all()
    return render_template('todo.html', tasks=tasks)


@app.route("/api/task", methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    tasks_data = [task.to_dict() for task in tasks]
    return jsonify(tasks_data)


@app.route("/api/task", methods=['POST'])
def create_task():
    task_name = request.json["name"]
    task = Task(name= task_name)
    db.session.add(task)
    db.session.commit()
    response_data = jsonify(task.to_dict())
    return make_response(response_data, 201)

@app.route("/api/task/<int:task_id>", methods=['GET'])
def task_details(task_id):
    task = Task.query.get(task_id)
    print(task)
    if task is None:
        return make_response("", 404)
    else:
        return jsonify(task.to_dict())

@app.route("/api/task/<int:task_id>", methods=['PUT'])
def modify_task(task_id):
    '''1. pobieramy zadanie z bazy
    2. pobieramy nową nazwę
    3. aktualizujemy baze
    '''
    task = Task.query.get_or_404(task_id)   # to samo co task details tylko jako wbudowana funkcja
    task.name = request.json["name"]
    db.session.commit()
    return jsonify(task.to_dict())

@app.route("/api/task/<int:task_id>", methods=["DELETE"])
def del_task(task_id):
    task =  Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return make_response("", 204)