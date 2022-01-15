"""Helper function for determining potential appointments"""

from datetime import datetime, timedelta


def show_potential_appointments(date, start_time, end_time):
    if start_time:
        start_time = date + " " + start_time
    else:
        start_time = date + " " + '00:00'
    start_time = datetime.fromisoformat(start_time)

    # make sure appointment start times are on the half hour
    if start_time.minute != 30 or start_time.minute != 0:
        if start_time.minute < 30:
            start_time += timedelta(minutes=(30 - start_time.minute))
        else:
            start_time += timedelta(minutes=(60 - start_time.minute))

    if end_time:
        end_time = date + " " + end_time
    else:
        end_time = date + " " + '23:59'

    end_time = datetime.fromisoformat(end_time)

    potential_appointments = set()

    time_ = start_time

    while time_ < end_time:
        appointment_slot = time_
        potential_appointments.add(appointment_slot)
        time_ = time_ + timedelta(minutes=30)

    return potential_appointments
