import itertools
friends = 'Bob Dante Julian Martin'.split()


def friends_teams(frineds=friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        result = itertools.permutations(friends, team_size)
    else:
        result = itertools.combinations(friends, team_size)
    return list(result)


if __name__ == '__main__':
    print(friends_teams())