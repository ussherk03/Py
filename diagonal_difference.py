
if __name__ == '__main__':
    limit = int(input())
    big_arr = []

    for _ in range(limit):
        arr = list(map(int, input().split()))
        big_arr.append(arr)

    x1 = sum([big_arr[0][0], big_arr[1][1], big_arr[2][2]])
    x2 = sum([big_arr[2][0], big_arr[1][1], big_arr[0][2]])

    det = abs(x1 - x2)

    print(det)




