"""Server for app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify, send_from_directory)
from model import db, connect_to_db
# import crud
# import requests
# import json
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'saddfkjaksdjfka;lsdfzxcjewmr.,9324'
app.jinja_env.undefined = StrictUndefined


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True, port=5000)