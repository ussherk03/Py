import itertools
import operator
from operator import itemgetter, attrgetter

class Student:
    def ___init___(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_s = [
    ('Patrick', 'A', 12),
    ('Laurel', 'B', 11),
    ('McMahon', 'C', 13),
]
print(sorted(student_s, key=itemgetter(0)))
print(sorted(student_s, key=itemgetter(1)))
print(sorted(student_s, key=itemgetter(2)))
print(repr(student_s))


data = ["Griselda 'La Madrina' Blanco", 'Irmagrade Ilse Ilde Grese', 'Elizabeth Bathory', 'Mary Tudor']
pair = [('Batman', 'Wayne', 0), ('Spider-man', 'Parker', 1), ('Iron Man', 'Stark', 2), ('White Wolf', 'Barkey', 3)]
string = 'Meine NAME ist USSHER Kojo Kingsley ICH bin EINEN gut JUNGE!'
mix = [1, 'Irma Grese', 'Mary Tudor', 2, 3, 'La Madrina', 4]
print(operator.getitem(pair, 2))
print(operator.itemgetter(2, 3)(pair))
#print(operator.not_(a)) --> returns a True or False whether or not the object is empty or not, respectively