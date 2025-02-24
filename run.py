from flask import Flask
import os


app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "Olá estou na aplicação"
