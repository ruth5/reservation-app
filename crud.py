""" CRUD operations."""

from model import db, User, connect_to_db


def create_user(email):
    """Create and return a new user."""

    user = User(email=email)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user with that email if it exists, otherwise return None."""
    
    return User.query.filter_by(email=email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app, echo=False)