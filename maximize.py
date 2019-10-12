
if __name__ == '__main__':

    from itertools import product, combinations

    result = []

    k, m = map(int, input().split())

    for i in range(k):
        arr_ = list(map(int, input().split()))[1:]   # list
        print(arr_)
        q = list(product(arr_))

        result = list(map(lambda x: sum(i** 2 for i in x) % m, product(arr_)))
        print(result)

    result_ = list(combinations(result, 3))
    print(result_)

    a = [sum(element) % m for element in result_]
    print(a)

'''
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
'''





