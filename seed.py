from models import User, db
from app import app

db.drop_all()
db.create_all()

User.query.delete()

ry = User(first_name="Ryan", last_name="Seltz")
shishi = User(first_name="Ashira", last_name="Seltz")
ari = User(first_name="Aryeh", last_name="Seltz")
ash = User(first_name="Asher", last_name="Gordon")

db.session.add(ry)
db.session.add(shishi)
db.session.add(ari)
db.session.add(ash)
db.session.commit()
