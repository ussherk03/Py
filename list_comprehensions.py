## List Comprehensions

x = 2
y = 2
z = 2
n = 2
ar = []
p = 0

for i in range(x + 1):
    print([i])
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                ar.append([])
                ar[p] = [i, j, k]
                p += 1
pos0 = ar

# List Comprehensions makes crunches code and makes it neater

c


def return_two_decimal_places (num):
    q = "{:.2f}".format(num)
    return q

print(return_two_decimal_places(0.1))