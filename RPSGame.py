import random


class Player:
    def __init__(self, name):
        self.name = name


class Roll:
    def __init__(self, name, beat, defeat):
        self.name = name
        self.beat = beat
        self.defeat = defeat

    def can_defeat(self, roll):
        result = 'Defeat'
        if roll.name == self.name:
            result = 'Tie'
        elif roll.name in self.beat:
            result = 'Beat'
        return result


def print_header():
    print('-' * 45)
    print('Welcome to classic Rock, Paper, Scissors Game')
    print('-' * 45)


def build_the_three_rolls():
    result = [Roll('Rock', 'Scissors', 'Paper'),
              Roll('Scissors', 'Paper', 'Rock'),
              Roll('Paper', 'Rock', 'Scissors')]
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


def main():
    print_header()

    rolls = build_the_three_rolls()

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
        outcome = p1_roll.can_defeat(p2_roll)
        if outcome == 'Beat':
            print(player1.name + ' wins')
        elif outcome == 'Defeat':
            print(player2.name + ' wins')
        else:
            print(outcome)
        # display throws
        # display winner for this round

        count += 1

    # Compute who won

if __name__ == '__main__':
    main()