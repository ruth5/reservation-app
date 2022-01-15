# Melon Reservation App Overview
This melon reservation app allows users to schedule melon tastings. This was done for a practice takehome exercise.


# Structure
- `server.py` contains Flask server setup and all routes
- `appointments.py` contains a helper function that assists with determining appointment slots
- `model.py` set up of database that stores user info and appointments
- `crud.py` contains functions for interacting with the PostgreSQL database

# Running the app

- Set up an activate a python virtual environment:
    * `virtualenv env`
    * `source env/bin/activate`
- Install all dependencies:
    * `pip3 install -r requirements.txt`
- Set up and seed the database (NOTE: this will drop the database and create a new one. Do not run this script if you do not want to drop the database)
    * run `python3 recreate_and_seed_db.py`
- Start up the server and run the app!
    * run `python3 server.py`
    * Navigate `localhost:5001` to see the app in your browser
    * If you used the provided seed script, you can log in with test users: user0@test.com, user1@test.com, etc. up to user9@test.com