from datetime import datetime
from datetime import timedelta
import time


def pomodoro_timer(duration):
    p_break = True
    time_start = datetime.now()
    while p_break:
        time.sleep(1)
        delta = datetime.now() - time_start
        print('.', end='', flush=True)
        if int(delta.seconds) > duration - 1:
            print('')
            p_break = False


if __name__ == '__main__':
    '''Original technique steps:
       Decide on the task to be done.
       Set the pomodoro timer (traditionally to 25 minutes).
       Work on the task.
       End work when the timer rings and put a checkmark on a piece of paper.
       If you have fewer than four checkmarks, take a short break (3–5 minutes), then go to step 2.
       After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1.'''
    tasks = []
    repeat = True
    while repeat:
        task = input('Enter task: ')
        tasks.append(task)
        print('Pomodoro timer started')
        pomodoro_timer(25)
        print('\a')
        print('Finish your task')
        repeat_reply = input('One more? (y/n): ')
        if repeat_reply != 'y':
            repeat = False
        else:
            if len(tasks) < 4:
                print("Time for short rest (10 sec)")
                pomodoro_timer(10)
            else:
                print('Tine for longer break (15 sec)')
                pomodoro_timer(15)
