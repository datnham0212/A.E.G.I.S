import datetime

def getCurrentDate():
    return datetime.datetime.now().strftime("%B %d, %Y")

def getCurrentDayInWeek():
    return datetime.datetime.now().strftime("%A")

def getFullDateMessage():
    day_name = getCurrentDayInWeek()
    date_string = getCurrentDate()
    return f"Today's {day_name}, {date_string} sir."


