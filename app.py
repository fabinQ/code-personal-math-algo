from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"


@app.route("/czesc")
def czesc():
    return """
        <html>
        <head><title>Czesc!</title></head>
        <body>
            <h1>Cześć wam!</h1>
            </body>
            </html>
    """


@app.route("/hej/<imie>")
def powitanie(imie):
    return f"Cześć, {imie}"


@app.route("/users/<int:id>")
def info_users(id):
    return f"Dane użytkownika o id {id}"