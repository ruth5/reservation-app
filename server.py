"""Server for app."""
from datetime import datetime

from flask import (Flask, render_template, request, flash, session, redirect, jsonify, send_from_directory)
from model import db, connect_to_db
import crud
# import requests
# import json
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'saddfkjaksdjfka;lsdfzxcjewmr.,9324'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def show_homepage():
    """View the homepage."""

    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login_user():
    """Log in a user."""

    email = request.form.get('email')
    user = crud.get_user_by_email(email)

    if user:
        flash(f"You are logged in, {email}")
        session['user_id'] = user.user_id
        print(session)
    else:
        flash(f"There is no account associated with that email.")
    
    return redirect('/')

@app.route('/appointment-search')
def appointment_search():
    """Show the appointment search page."""

    return render_template('appointment-search.html')

@app.route('/appointment-search', methods = ['POST'])
def show_available_reservations():
    """Show available appointments based on search paramters"""

    return render_template('appointment-search.html')


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True, port=5001)
