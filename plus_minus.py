
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    print(arr)

    x = y = z = 0

    for _ in arr:
        if _ > 0:
            x += 1

        elif _ < 0:
            y += 1

        else:
            z += 1

    result = [x/n, y/n, z/n]

    for i in result:
        print("{0:2f}".format(i))

'''
6
-4 3 -9 0 4 1
'''
