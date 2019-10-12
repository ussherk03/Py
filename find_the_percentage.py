
if __name__ == '__main__':
    n = int(input())
    d = []

    for _ in range(n):
        s = input().split()
        name = s[0: 1][0]

        scores = sum(list(map(float, s[1:]))) / 3
        final_mean = '{:2f}'.format(scores)
        result = [name, float(final_mean)]
        d.append(result)

    q = dict(d)

    print(q[input()])




'''
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
'''