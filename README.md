# Melon Tasting Reservation App Overview
This melon tasting reservation app allows users to schedule melon tastings. This was done for a practice takehome exercise.

The prompt stated the requirements: "We offer coverage 24/7/365 (including weekends and holidays) but only 1 user can book an appointment on a given day and time. 		

The service has these requirements:
 * all reservations must start and end on the hour or half hour
 * all reservations are exactly 30 minutes long
 * a user can only have 1 reservation on a calendar date (#tooMuchMelon)
If these conditions cannot be met (for example the user has already booked an appointment on the chosen date), show an error message indicating that."


# Structure
- `server.py` contains Flask server setup and all routes
- `appointments.py` contains a helper function that assists with determining appointment slots
- `model.py` set up of database that stores user info and reservations
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

# Next steps

If I had more time to complete this exercise, I would prioritize the following as I worked to improve the app:
- Deploy the site
- Add tests, including unit tests and integration tests
- Improve the styling of the app