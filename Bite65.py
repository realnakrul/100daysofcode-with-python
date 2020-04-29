import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
if not os.path.exists(DICTIONARY):
    urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY)


with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


LETTERS = ['E', 'P', 'A', 'E', 'I', 'O', 'A']
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Calc the max value of a collection of words"""
    result = []
    for word in words:
        if calc_word_value(word) == calc_word_value(max(words, key=calc_word_value)):
            # TODO: switch to list comprehensions
            result.append(word)
    return result


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    result = []
    for l in range(1, len(draw)+1):
        for w in _get_permutations_draw(draw, l):
            candidate = ''.join(w).lower()
            # print(candidate)
            if candidate in dictionary and candidate not in result:
                result.append(candidate)

    return max_word_value(result)


def _get_permutations_draw(draw, len):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    # TODO: try with generator, not list
    result = itertools.permutations(draw, len)
    return list(result)


if __name__ == '__main__':
    print(get_possible_dict_words(LETTERS))