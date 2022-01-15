"""Seeds the database with 10 test users."""

import os

import crud, model, server

os.system('dropdb melon_reservations')
os.system('createdb melon_reservations')

model.connect_to_db(server.app, echo=False)
model.db.create_all()

for n in range(10):
    email = f'user{n}@test.com' 

    user = crud.create_user(email)
