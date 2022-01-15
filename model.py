"""Data models for app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
   
    def __repr__(self):
        return f"<User id={self.user_id} email={self.email}>" 

class Reservation(db.Model):
    """A reservation."""

    __tablename__ = "reservations"
    res_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    res_start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Reservation id={self.res_id} user_id={self.user_id} res_start_time={self.res_start_time}>"


my_db_name = "melon_reservations"

def connect_to_db(flask_app, db_uri=f"postgresql:///{my_db_name}", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app, echo=False)


