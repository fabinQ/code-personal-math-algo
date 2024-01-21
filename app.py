from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("glowna.html")

@app.route("/czesc")
@app.route("/czesc/<imie>")
def czesc(imie=None):
    return render_template("czesc.html",imie=imie)

@app.route("/users/<int:id>")
def info_user(id):
    return f'Dane użytkownika o id: {id}'

tasks = [
    "Zrobić zakupy",
    "Posprzątać mieszkanie"
]
@app.route("/todo", methods=['GET','POST'])
def todo():
    if request.method == 'POST':
        # request.form - słownik z naszego pola ze wszystkich inputów
        tasks.append(request.form['task'])
    return render_template('todo.html', tasks=tasks)

