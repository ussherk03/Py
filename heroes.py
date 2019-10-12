# Create a class that will print out each member of a and b in the form x, y eg. Bruce Wayne, Batman
# Secondly, the class--you created--must have the '__next__' method to print the next member of the  dictionary you will
#... obtain anytime the next function is used outside the class

import random

a = ['Bruce Wayne', 'Clark Kent', 'Barry Allen', 'Peter Parker', 'Tony Stark', 'Steve Rogers', 'Wade', 'Oliver Queen']

b = ['Batman', 'Superman', 'Flash', 'Spider man', 'Iron Man', 'Captain America', 'Deadpool', 'Green Arrow']

c = [x for x in range(9)]


class Heroes:

    def __init__(self, name, hero):
        self.value = list(name)
        self.hero = list(hero)
        #self.amount = amount

    def __iter__(self):
        match = dict(zip(list(self.value), list(self.hero)))
        print(match)

    def __next__(self):
        remindd = list(zip(tuple(self.value), tuple(self.hero)))
        it = list(iter(remindd))
        a = 0
        for i in it:
            return i
        a += 1


pair = Heroes(a, b)
print(next(pair))
```
``
# try:
#     for i in pair:
#         print(i)
#     print(pair)
# except TypeError:
#     pass
