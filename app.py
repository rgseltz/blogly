"""Blogly application."""

from flask import Flask, render_template, request, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'monkeyboy25'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_user_list():
    users = User.query.order_by(User.first_name, User.last_name).all()
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
    posts = user.posts
    return render_template('user.html', user=user, posts=posts)


@app.route('/edit-user/<int:user_id>')
def edit_user(user_id):
    user = User.query.get(user_id)
    # first = user.first_name
    # last = user.last_name
    # image_url = user.image_url
    print(f'$$%%%%%%{user}#$#%$$^$%%$^')
    return render_template('edit-user.html', user=user)


@app.route('/edit-user/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.add(user)
    db.session.commit()

    return redirect('/')


@app.route('/user/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')


@app.route('/user/<int:user_id>/posts/new')
def get_post_form(user_id):
    user = User.query.get(user_id)
    return render_template('posts.html', user=user)


@app.route('/user/<int:user_id>/posts/new', methods=["POST"])
def upload_new_post(user_id):
    user = User.query.get(user_id)
    title = request.form['title']
    content = request.form['content']
    post = Post(title=title, content=content, user_id=int(user_id))
    print(f'$%#$$%^$#^#$^{post}##%#$%@%^$^')
    print(f'#$#$$$%$^$%%${title}AND {content}%%%%%^^$#%$$$##$$%')
    db.session.add(post)
    db.session.commit()
    user_posts = Post.query.filter(Post.user_id == user_id).all()
    return render_template('user.html', posts=user_posts, user=user)


@app.route('/user/<int:user_id>/post/<int:post_id>')
def show_post_detail(user_id, post_id):
    user = User.query.get(user_id)
    post = Post.query.get(post_id)
    return render_template('post-detail.html', user=user, post=post)


@app.route('/user/<int:user_id>/post/<int:post_id>/delete', methods=["POST"])
def delete_post(user_id, post_id):
    post = Post.query.get_or_404(post_id)
    print(f'$$%%%%%%%%%%{post}$$$$$%%%%%%%^^%')
    db.session.delete(post)
    db.session.commit()
    return redirect(f'/user/{user_id}')


@app.route('/user/<int:user_id>/post/<int:post_id>/edit')
def get_edit_post_form(user_id, post_id):
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    return render_template('edit-post.html', post=post, user=user)


@app.route('/user/<int:user_id>/post/<int:post_id>/edit', methods=["POST"])
def update_post_form(user_id, post_id):
    user = User.query.get(user_id)
    post = Post.query.get(post_id)

    post.title = request.form["title"]
    post.content = request.form["content"]

    db.session.add(post)
    db.session.commit()
    return redirect(f'/user/{user.id}')
