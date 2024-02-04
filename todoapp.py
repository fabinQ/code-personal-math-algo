from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine
import os


file_path = os.path.join(os.path.abspath(os.getcwd()), 'temp', 'todo2.db')
print(file_path)

engine = create_engine("sqlite:///todo2.db")
metadata_obj = MetaData()


app = Flask(__name__)
# Ustalamy gdzie będzie nasza baza danych. Robimy to przez app.config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + file_path
db = SQLAlchemy(app)


'''Tworzymy model, który będzie reprezentowała table w bazie danych.
    Pola w tej klasie reprezentują kolumny w odpowiedniej tabeli'''
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)



@app.route("/", methods=['GET','POST'])
def todo():
    if request.method == 'POST':
        new_task = Task(name=request.form['task'])
        db.session.add(new_task)
        db.session.commit()

    tasks = Task.query.all()
    return render_template('todo.html', tasks=tasks)

with app.app_context():
    # Inicjalizacja bazy danych
    db.create_all()
