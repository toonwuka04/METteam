from flask import Flask, render_template, sessions, url_for, redirect, request, session, flash
from flask.helpers import flash
import os
from werkzeug.utils import secure_filename
from functools import wraps

#create a flask app
app = Flask(__name__)
app.secret_key = 'fjalkfjlkdsfja;kdsfld'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash('You need to log in first')
            return redirect(url_for('login'))
    return wrap

#define a route
#can name multiple route
@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods = ['GET', "POST"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid credentials, please try again'
        else:
            session['logged_in'] = True
            flash('You are logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error = error)

@app.route("/designCourse")
def designCourse():
    return render_template("designCourse.html")

@app.route("/designCourse", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        flash("No file found")
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No file selected for uploading')
        return redirect(request.url)
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_video filename: ' + filename)
        flash('File successfully uploaded and displayed below')
        return render_template('designCourse.html', filename=filename)

@app.route('/designCourse/<filename>')
def display_video(filename):
	#print('display_video filename: ' + filename)
	return filename

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You are logged out!')
    return redirect(url_for('welcome'))

if __name__ == "__main__":
    app.run(debug=True)