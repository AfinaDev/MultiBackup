import sys
import time


def spinner(msg: str, stop_event):
    symbols = ['|', '/', '-', '\\']
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{msg} {symbols[idx]}")
        sys.stdout.flush()
        idx = (idx + 1) % len(symbols)
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 40 + "\r")