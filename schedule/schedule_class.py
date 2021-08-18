#schedule_class
#link of tutorial: Live de Python #50 - Agendando tarefas com python  |  https://www.youtube.com/watch?v=FjJ1bClIa-o

import sched
import time
# time.ctime()

scheduler = sched.scheduler()

def saytime():
    print(time.ctime())
    scheduler.enter(delay=10, priority=0, action=saytime)

saytime()

scheduler.run(blocking=True)
