#'check' compares to words and tells whether or not they have the same ending of
# of x and y


def check(x, y):
    if x[-2:] == y[-2:]:
        print('They both end with "-{}"'.format(x[-2:]))

    else:
        print('"-{}" and "-{}" are both different endings.'.format(x[-2:], y[-2:]))


check('Ronaldinho', 'Ronaldo')
check('Isis', 'Persis')
check('Lina', 'Ussher')
