from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# Musimy ustalić gdzie będzie nasza baza danych. Dla innych baz trzeba wpisać użytkownika i hasło
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)

@app.route("/p", methods=['GET','POST'])
def todo():
    task = []
        if request.method == 'POST':
            task.append(request.from['task'])
        return render_template('todo.html', tasks=tasks)