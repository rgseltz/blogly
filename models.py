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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    user = db.relationship('User', backref='posts')

    def __repr__(self):
        return f'<Post id={self.id} title={self.title} content={self.content} created_at={self.created_at} user_id={self.user_id}'
