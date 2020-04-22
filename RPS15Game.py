import os
import random
from urllib.request import urlretrieve
import csv


def get_classes_file():
    BASE_URL = 'https://raw.githubusercontent.com/talkpython/100daysofcode-with-python-course/master/days/13-15-text-games/data/'
    TMP = '/tmp'

    fname = 'battle-table.csv'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    if not os.path.exists(local):
        urlretrieve(remote, local)
    return local


class Player:
    def __init__(self, name):
        self.name = name


class Roll:
    def __init__(self, name, can_defeat):
        self.name = name
        self.can_defeat = can_defeat


def print_header():
    print('-' * 45)
    print('Welcome to 15-way Rock, Paper, Scissors Game!')
    print('-' * 45)


def read_rolls(fname):
    with open(fname) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            read_roll(row)


def read_roll(row: dict):
    name = row['Attacker']
    del row['Attacker']
    del row[name]
    result = []

    for k in row.keys():
        can_defeat = row[k].strip().lower() == 'win'
        if can_defeat:
            result.append(k)
    return Roll(name, result)


def build_rolls(fname):
    result = []
    with open(fname) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            result.append(read_roll(row))
    return result


def get_players_name():
    result = input('Enter your name:\n')
    return result


def get_player_roll(rolls):
    correct_input = False
    print('\nEnter number of a desired roll:')
    for n, r in enumerate(rolls):
        print(str(n) + ' -', r.name)
    while not correct_input:

        try:
            p_roll = int(input())
            if p_roll in range(len(rolls)):
                result = rolls[int(p_roll)]
                correct_input = True
        except Exception as e:
            print('Incorrect input, enter number in range 0..' + str(len(rolls)-1))

    return result


def who_won(p1, p2, r1, r2):
    if r1.name == r2.name:
        result = 'Tie'
    elif r2.name in r1.can_defeat:
        result = (p1.name + ' wins')
    else:
        result = (p2.name + ' wins')
    return result


def main():
    print_header()
    rolls = build_rolls(get_classes_file())

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Computer")

    game_loop(player1, player2, rolls)


def game_loop(player1, player2, rolls):
    count = 1
    while count <= 3:
        print('\nRound:', count)
        p2_roll = random.choice(rolls)
        p1_roll = get_player_roll(rolls)
        print('\nThrows:')
        print(player1.name, ':', p1_roll.name)
        print(player2.name, ':', p2_roll.name)
        print(who_won(player1, player2, p1_roll, p2_roll))

        count += 1


if __name__ == '__main__':
    main()
