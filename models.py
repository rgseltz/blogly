"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import ForeignKey

db = SQLAlchemy()


def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)


class User(db.Model):
    """Make user entries"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String, nullable=False)

    last_name = db.Column(db.String, nullable=False)

    image_url = db.Column(db.String, nullable=True,
                          default='https://images.emojiterra.com/google/noto-emoji/v2.034/128px/1f609.png')

    def __repr__(self):
        return f"<User first_name={self.first_name}, last_name={self.last_name}, image={self.image_url}>"


class Post(db.Model):
    """Posts Model"""

    __tablename__ = 'posts'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='posts')
    # tags = db.relationship('Tag', secondary=('posts_tags'), backref=('posts'))

    def __repr__(self):
        return f'<Post id={self.id} title={self.title} content={self.content} created_at={self.created_at} user_id={self.user_id}'


class PostTag(db.Model):
    """Post_Tag Model"""

    __tablename__ = 'posts_tags'
    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    # user_id = db.Column(db.Integer, ForeignKey('users.id'))


class Tag(db.Model):
    """Tag Model"""

    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)

    post = db.relationship('Post', secondary="posts_tags", backref="tags")
    # user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)

    # user = db.relationship('User', secondary=('posts_tags'), backref=('user_tags'))

    def __repr__(self):
        return f'<Tag id={self.id} name={self.name}>'
