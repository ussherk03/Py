
# Factorial of n means n! = n * (n-1) * (n-2) * (n-3) ... * 1

def factorial_of_n():
    n = int(input('Enter number here: '))

    q = list(range(1, n + 1))

    for i in range(len(q)):
        q[0] *= q[i]
    return q[0]

print(factorial_of_n())















