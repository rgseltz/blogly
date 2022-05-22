"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

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
