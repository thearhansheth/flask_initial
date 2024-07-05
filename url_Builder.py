from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    return 'Welcome Back Admin'

@app.route('/Guest/<guest>')
def Guest(guest):
    return 'Hello %s' %guest

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('Guest', guest = name))

app.run(debug = True)