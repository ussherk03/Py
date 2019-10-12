
def string_formats ():
    number = int(input('Enter number: '))

    start = 1
    stop = number + 1

    for _ in range(start, stop):
        print('{0:>{w}d} {0:>{w}o} {0:>{w}X} {0:>{w}b}'.format(_, w=len(bin(number))))

string_formats()

