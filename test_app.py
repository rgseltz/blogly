from unittest import TestCase

from app import app
from models import db, User, Post

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_blogly'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UsersTestCase(TestCase):
    def setUp(self):
        """Add sample user."""

        User.query.delete()

        user = User(first_name="Shimi", last_name="Hymanzweig")

        db.session.add(user)
        db.session.commit()

        self.user_id = user.id
