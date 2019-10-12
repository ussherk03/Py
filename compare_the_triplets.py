
def compare_the_triplets ():
    result = [0, 0]

    a = map(int, input().split())
    b = map(int, input().split())

    pack = list(zip(a, b))

    for elements in pack:
        if elements[0]  > elements[1]:
            result[0] += 1
        elif elements [0] < elements[1]:
            result[1] += 1
        else:
            result[0] += 0
            result[1] += 0


    return ' '.join([repr(i) for i in result])

scores = compare_the_triplets()

print(scores)
