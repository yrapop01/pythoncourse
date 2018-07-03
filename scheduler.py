from multiprocessing import Process
from datetime import datetime, timedelta
import time

class Scheduler:
    def __init__(self):
        self._tasks = []

    def task(self, timestr):
        def inner(func):
            self.add(timestr, func)
            return func

        return inner

    def add(self, timestr, func):
        assert len(timestr) == len('XX:XX')
        assert timestr[2] == ':'

        if 'X' in timestr:
            s = timestr.replace(':', '')
            i = s.rindex('X')
            assert s[:i] == 'X' * i and s[i + 1:].isdigit()

        self._tasks.append((timestr, func))

    def run(self):
        processes = []

        for timestr, func in self._tasks:
            p = Process(target=run_task, args=(timestr, func), daemon=False)
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

def grid24(timestr):
    hourstr = timestr[:2]
    minutestr = timestr[-2:]

    if hourstr == 'XX':
        hours = list(range(24))
    elif hourstr[0] == 'X':
        n = int(hourstr[1])
        hours = [n, 10 + n]
        if n <= 3:
            hours += [20 + n]
    else:
        hours = [int(hourstr)]

    if minutestr == 'XX':
        minutes = list(range(60))
    elif minutestr[0] == 'X':
        n = int(minutestr[1])
        minutes = [i + n for i in range(0, 60, 10)]
    else:
        minutes = [int(minutestr)]

    grid = [h * 60 * 60 + m * 60 for h in hours for m in minutes]
    return [timedelta(seconds=s) for s in grid]

def wait_for(event):
    now = datetime.now()
    print('Waiting for', event, (event - now).total_seconds(), 'seconds', flush=True)
    if event > now:
        time.sleep((event - now).total_seconds())

def run_task(timestr, func):
    grid = grid24(timestr)[::-1]

    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    events = [midnight + event for event in grid if midnight + event >= now]

    while True:
        while events:
            wait_for(events.pop())
            func()

        midnight += timedelta(1)
        events = [midnight + event for event in grid]
        wait_for(midnight)
