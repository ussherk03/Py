
def fibonacci(n):
    # return a list of fibonacci numbers
    q = [0, 1]

    for _ in range(2,n):
        q.append(q[_-1] + q[_-2])

    return q[0:n]

print(fibonacci(10))