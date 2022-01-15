""" CRUD operations."""

from model import db, User, Reservation, connect_to_db


def create_user(email):
    """Create and return a new user."""

    user = User(email=email)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user with that email if it exists, otherwise return None."""
    
    return User.query.filter_by(email=email).first()

def create_reservation(user_id, res_start_time):
    """Create and return a new reservation."""

    reservation = Reservation(user_id=user_id, res_start_time=res_start_time)

    db.session.add(reservation)
    db.session.commit()

    return reservation

def get_reservations_by_time_range(start_time, end_time):
    """Return reservations in the given time range."""
    
    reservations_in_range = Reservation.query.filter((Reservation.res_start_time >= start_time) & 
        (Reservation.res_start_time <= end_time)).all()

    return reservations_in_range

def check_if_conflicting_res(start_time, end_time, user_id):
    """Return True if user has a reservation in that time range. Otherwise return False."""
    
    first_reservation_in_range = Reservation.query.filter((Reservation.res_start_time >= start_time) & 
        (Reservation.res_start_time <= end_time) & (Reservation.user_id == user_id)).first()

    if first_reservation_in_range:
        return True
    else:
        return False




if __name__ == '__main__':
    from server import app
    connect_to_db(app, echo=False)