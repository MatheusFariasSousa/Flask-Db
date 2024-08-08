from flask import Flask

app = Flask(__name__)

dicionario = {}

@app.route("/")
def hello_world():
    return f"hello World"

@app.route("/dicionario")
def get_db():
    return dicionario

@app.route("/dicionario/post/<nome>/<idade>")
def post_db(nome:str,idade:int):
    dicionario[nome]=idade
    return "sucess"

@app.route("/dicionario/delete/<nome>")
def delete_db(nome:str):
    if nome in dicionario:
        del dicionario[nome]
        return "sucess"
    return "this is not a valid name"

@app.route("/dicionario/put/<nome>/<idade>")
def put_db(nome:str,idade:int):
    if nome in dicionario:
        dicionario[nome]=idade
        return "sucess"

    return "this is not a valid name"
