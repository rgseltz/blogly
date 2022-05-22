"""Blogly application."""

from flask import Flask, render_template, request, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'monkeyboy25'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_user_list():
    users = User.query.all()
    return render_template('list.html', users=users)


@app.route('/', methods=['POST'])
def create_user():
    first = request.form["first_name"]
    last = request.form["last_name"]
    image_url = request.form["image_url"]
    if image_url == "":
        image_url = None
    print(f'$$$$$%%%%%%%&&&&{image_url}$$$$$%%%%%%%^^^^')

    user = User(first_name=first, last_name=last, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/user/{user.id}")


@app.route('/user/<int:user_id>')
def show_user(user_id):
    user = User.query.get(user_id)
    return render_template('user.html', user=user)


@app.route('/edit-user/<int:user_id>')
def edit_user(user_id):
    user = User.query.get(user_id)
    # first = user.first_name
    # last = user.last_name
    # image_url = user.image_url
    print(f'$$%%%%%%{user}#$#%$$^$%%$^')
    return render_template('edit-user.html', user=user)
