from flask import Flask, render_template, request
import os
app = Flask(__name__)
app.secret_key = 'rewqurieru23ew'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/tutorspage")
def tutorspage():
    return render_template("tutorspage.html")

if __name__ == "__main__":
    app.run(debug=True)