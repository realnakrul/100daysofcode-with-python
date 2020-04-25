from random import choice

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def gen_pairs(names=NAMES):
    for n in names:
        a = choice(names)
        while n == a:
            a = choice(names)
        result = '{} teams up with {}'
        yield result.format(n.split()[0], a.split()[0])


if __name__ == '__main__':
    titles = [name.title() for name in NAMES]
    print(titles)
    reverse = [name.split()[1].capitalize() + ' ' + name.split()[0].capitalize() for name in NAMES]
    print(reverse)

    pairs = gen_pairs(titles)
    for _ in range(10):
        print(next(pairs))
