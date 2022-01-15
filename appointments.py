from datetime import datetime, timedelta


def show_potential_appointments(date, start_time, end_time):
    if start_time:
        start_time = date + " " + start_time
    else:
        start_time = date + " " + '00:00'
    start_time = datetime.fromisoformat(start_time)

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
        time_ = time_ + timedelta(minutes = 30)
    

    return potential_appointments

