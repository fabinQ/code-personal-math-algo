from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine

engine = create_engine("sqlite:///todo2.db")
metadata_obj = MetaData()


app = Flask(__name__)
# Ustalamy gdzie będzie nasza baza danych. Robimy to przez app.config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////temp/todo2.db"
db = SQLAlchemy(app)


'''Tworzymy model, który będzie reprezentowała table w bazie danych.
    Pola w tej klasie reprezentują kolumny w odpowiedniej tabeli'''
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)



@app.route("/", methods=['GET','POST'])
def todo():
    tasks = []
    if request.method == 'POST':
        # request.form - słownik z naszego pola ze wszystkich inputów
        tasks.append(request.form['task'])
    return render_template('todo.html', tasks=tasks)

with app.app_context():
    # Inicjalizacja bazy danych
    db.create_all()
