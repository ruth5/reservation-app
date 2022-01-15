"""Server for app."""
from datetime import datetime
from appointments import show_potential_appointments

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'saddfkjaksdjfka;lsdfzxcjewmr.,9324'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """View the homepage."""

    if 'user_id' in session:
        return redirect('/appointment-search')

    return render_template('index.html')


@app.route('/login', methods=['POST'])
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


@app.route('/log-out')
def clear_session():
    """Log out the user."""

    if "user_id" in session:
        session.clear()
        flash("You have been logged out.")

    return redirect('/')


@app.route('/appointment-search')
def appointment_search():
    """Show the appointment search page."""

    return render_template('appointment-search.html')


@app.route('/appointment-search', methods=['POST'])
def show_available_reservations():
    """Show available appointments based on search paramters"""

    date = request.form.get('date')

    start_of_day = date + " 00:00"
    start_of_day = datetime.fromisoformat(start_of_day)
    end_of_day = date + " 23:59"
    end_of_day = datetime.fromisoformat(end_of_day)

    if crud.check_if_conflicting_res(start_of_day, end_of_day, session['user_id']):
        flash("Sorry, you've already booked an appointment on that day. Only one appointment per day allowed.")
        return redirect('/appointment-search')

    start_time = request.form.get('start-time')

    end_time = request.form.get('end-time')

    appointment_results = show_potential_appointments(
        date, start_time, end_time)
    appointment_results_sorted = sorted(list(appointment_results))
    potential_conflicts = crud.get_reservations_by_time_range(
        appointment_results_sorted[0], appointment_results_sorted[-1])
    potential_conflict_times = {
        reservation.res_start_time for reservation in potential_conflicts}

    available_appointments = appointment_results - potential_conflict_times

    if not available_appointments:
        flash("Sorry, no appointments are available in that time range. Please try again.")
        return redirect('/appointment-search')

    available_appointments_sorted = sorted(list(available_appointments))

    # need isoformat because can't have space in value for HTML tag
    appointments_reg_to_iso = {}
    for appointment in available_appointments_sorted:
        appointments_reg_to_iso[appointment] = appointment.isoformat()

    return render_template('appointment-results.html', appointments_reg_to_iso=appointments_reg_to_iso)


@app.route('/appointment-results', methods=['POST'])
def book_appointment():
    """Books the appointment the user selected using the book appointment button"""

    booked_res = request.form.get('booked-res')
    reservation = crud.create_reservation(session['user_id'], booked_res)

    flash(f"Booked this reservation: {reservation.res_start_time}")
    return redirect('/scheduled-appointments')


@app.route('/scheduled-appointments')
def show_all_user_appointments():
    """Page that shows all tastings a user has booked."""

    booked_appointments_by_user = crud.get_appointments_by_user(
        session['user_id'])
    appointment_times = [
        reservation.res_start_time for reservation in booked_appointments_by_user]
    if appointment_times:
        appointment_times.sort()

    return render_template('scheduled-appointments.html', appointments=appointment_times)


if __name__ == "__main__":
    connect_to_db(app, echo=False)
    app.run(host="0.0.0.0", debug=True, port=5001)
