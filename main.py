from flask import Flask, render_template, request
import os

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")
