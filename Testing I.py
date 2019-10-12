import itertools

#Prototype to model which is in Testing.py
numbers = '362'
a = list(itertools.permutations(numbers, 1))

hand = []
for tup in a:
    for index in tup:
        hand.append(index)
print(hand)

b = list(itertools.permutations(numbers, 2))
toes = []
for put in b:
    toes.append(put)

c = list(itertools.permutations(numbers, 3))
fingers = []
for tap in c:
    fingers.append(tap)

##Merge hand, toes and fingers
merger = list(itertools.chain(hand, toes, fingers))
integers = [int(string) for string in merger]
loyals = list(itertools.filterfalse(lambda x:x%3, integers))

traitors = list((set(integers) - set(loyals)))
traitors.sort()
print(traitors)
print(loyals)
maximum_num = []
result = []
result[len(result):] = len(loyals), loyals[-1]
print(result)


















































































































'''numbers = [1,2,3,4,5,6,7,8,9]
one = [64,36,9,4,81,1,25,49,16]
two = [64,121,9,4,81,1,25,49,16]

#In this function, [list a] == [list b] only if the members of "b" are the exact squares of each element of "a" regardless of the order.
def comparable(a, b):
    # convert b into a set()
    theoretical_squares = set(b)
    # create a set of squares from 'a' so that it can be compared with 'theoretical squares', which is formed from 'b'
    real_squares = set(map(lambda x:x**2, a))
    # the conditions below checks if the two sets contain the same elements or vice versa to confirm the comparison
    # between 'a' and 'b'
    if theoretical_squares - real_squares == set():
        print('Hurray, they are equal')
    else:
        print("Merlin's beard, they ain't equal.")

comparable(numbers, one) #compares the two lists in favour of the if-statement '''
































