import itertools
import time
import random


LIGHT_COLORS = ['RED', 'GREEN', 'YELLOW']


def draw_light(color, duration):
    traffic_light = '\n+-+\n|{}|\n+-+\n|{}|\n+-+\n|{}|\n+-+\n'
    print('{} for {} seconds'.format(color, duration))
    if color == 'RED':
        print(traffic_light.format('O', ' ', ' '))
    elif color == 'YELLOW':
        print(traffic_light.format(' ', '0', ' '))
    elif color == 'GREEN':
        print(traffic_light.format(' ', ' ', '0'))
    else:
        print('Traffic light broken!')
    time.sleep(duration)


if __name__ == '__main__':
    lights = itertools.cycle(LIGHT_COLORS)
    while True:
        current_light = next(lights)
        if current_light == 'YELLOW':
            delay = 5
        else:
            delay = random.randint(10, 20)
        draw_light(current_light, delay)


