from unittest import TestCase
from app import app

from models import db, User, Post

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_blogly'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Tests for model for User"""

    def setUp(self):
        """Clean any existing users"""

        User.query.delete()

    def tearDown(self):
        """Clean up added data at end of tests"""

        db.session.rollback()

    def create_new_User(self):
        user = User(first_name="Alex", last_name="Strongwater")

        self.assertEquals(user.first_name, "Alex")
        self.assertEquals(user.last_name, "Strongwater")

        db.session.add(user)
        db.session.commit()

    def edit_user(self):
        user = User(first_name="test-first", last_name="test-last")

        user.last_name = "Test3"

        self.assertEquals(user.last_name, "Test3")

        db.session.add(user)
        db.session.commit()

    def delete_user(self):
        user = User(first_name="test-first", last_name="test-last")

        user.last_name = "Test3"

        self.assertEquals(user.last_name, "Test3")

        db.session.add(user)
        db.session.commit()
        db.session.delete(user)

        # self.assertIn()


# class PostModelTestCase(TestCase):
#     def setUp(self):
#         """Clean any existing posts"""

#         Post.query.delete()

#     def tearDown(self):
#         """Clean up messed up data at end of test"""

#         db.session.rollback()
