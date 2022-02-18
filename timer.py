import time
from threading import Thread

timer_is_on = True
seconds = None


def timer():
    global seconds, timer_is_on
    set_time = time.time()
    while timer_is_on:
        ctime = time.time()
        seconds = int(ctime - set_time)
        time.sleep(1)
