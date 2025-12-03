import schedule
import time

def scheduler(func, hour: int = 6):
    func()

    schedule.every(hour).hours.do(func)
    while True:
        schedule.run_pending()
        time.sleep(1)
