
# count_odd(n) returns the number of odd numbers below n itself.
def count_odd(n):
    list_of_odd = list(range(1, n, 2))

    return list_of_odd

print(count_odd(15))