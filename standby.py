import datetime


def stabdby_mode(from_hour, to_hour):
    now = datetime.datetime.now().time()

    if from_hour <= now.hour <= to_hour :
        return True
    else:
        return False
