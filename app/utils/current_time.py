from datetime import datetime

def current_time():
    now = datetime.now()
    return now.strftime("%d_%m_%Y_%H_%M")