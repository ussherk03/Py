

def create_rug_faster(dimension):
    sticks = '.|.'
    a = 1
    n, m = map(int, dimension.split(' '))
    for i in range(round((n -1) / 2)):
        global array
        array = [((sticks * a).center(m, '-'))]
        print((sticks * a).center(m, '-'))
        a += 2

        if i == round(((n - 1) / 2) - 1):
            print('WELCOME'.center(m, '-'))

    b = round((n -1) / 2) + round(((n - 1) / 2) - 1)
    for _  in range(round((n -1) / 2)):
        print((sticks * b).center(m, '-'))
        b -= 2

create_rug_faster('99 297')


