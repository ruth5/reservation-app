""" CRUD operations."""

from model import db, User, connect_to_db


def create_user(email, password, first_name=None, last_name=None, home_zip_code=None):
    """Create and return a new user."""

    user = User(email=email, password=password, first_name=first_name, last_name=last_name, home_zip_code=home_zip_code)

    db.session.add(user)
    db.session.commit()

    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app, echo=False)