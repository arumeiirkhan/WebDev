def alarm_clock(day, vacation):
    if vacation:
        return "10:00" if day in [1, 2, 3, 4, 5] else "off"
    else:
        return "7:00" if day in [1, 2, 3, 4, 5] else "10:00"
