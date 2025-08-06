# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials
USERNAME = "admin"
PASSWORD = "password123"

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            error = "Invalid credentials. Please try again."
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7500)
