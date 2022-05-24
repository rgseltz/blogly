from models import User, db, Post
from app import app

db.drop_all()
db.create_all()

User.query.delete()
Post.query.delete()

ry = User(first_name="Ryan", last_name="Seltz")
shishi = User(first_name="Ashira", last_name="Seltz")
ari = User(first_name="Aryeh", last_name="Seltz")
ash = User(first_name="Asher", last_name="Gordon")
larry = User(first_name="Larry", last_name="David")
jerry = User(first_name="Jerry", last_name="Seinfeld")
forest = User(first_name="Forest", last_name="Whittaker")

db.session.add(ry)
db.session.add(shishi)
db.session.add(ari)
db.session.add(ash)
db.session.add(larry)
db.session.add(jerry)
db.session.add(forest)
db.session.commit()

p1 = Post(title="Life",
          content="laurem ipsum knows all the answers to all the questions", user_id=1)
p2 = Post(title="breath", content="to breathe is to live is to laugh", user_id=2)
p3 = Post(title="Towards a Better Tomorrow",
          content="Often, we have to face the reality of our situations", user_id=1)
p4 = Post(title="Goals",
          content="Only through hard work, clear vision, and perseverence, do we succeed", user_id=3)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)

db.session.commit()
