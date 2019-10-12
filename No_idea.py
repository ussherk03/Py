

if __name__ == '__main__':
    n, m = input().split(' ')
    s = input()
    set_s = set(s.split(' '))

    set_a = set(input().split(' '))
    set_b = set(input().split(' '))

    x = sum([(i in set_a) - (i in set_b) for i in set_s], 0)







