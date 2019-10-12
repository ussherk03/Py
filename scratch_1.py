from collections import deque

# Given an array of strings, reverse them and their order in such way that their length stays
# the same as the length of the original inputs.

a = ["I", "like", "big", "batts", "and", "I", "cannot", "lie!"]

def ultimate_array_reverser(x):
    print(x)

    b = []
    c = []
    d = []
    e = []
    s = list(reversed(x))

    for i in s:
        y = b.append(list(reversed(i)))

    for arr in b:
        c.append(''.join(arr))

    print(c)

    string_new = ''.join(c)

    print(string_new) # string-format of reversed-reversed list

    for string in x:
        d.append(len(string))
    print(d)
    print(list(reversed(d)))
    q = sum(d) # Sum of all integers in d



    print(string_new[0: 1])
    print(string_new[1: 5])
    print(string_new[5: 8])
    print(string_new[8: 13])
    print(string_new[13: 16])
    print(string_new[16: 17])
    print(string_new[17: 23])
    print(string_new[23: 27])
    print('******')






















ultimate_array_reverser(a)














