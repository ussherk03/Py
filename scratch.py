# Given an array of numbers, return a string made up of four parts:
# a) a four character 'word', made up of the characters derived from the first two and last two numbers in the array. order should be as read left to right (first, second, second last, last),
# b) the same as above, post sorting the array into ascending order,
# c) the same as above, post sorting the array into descending order,
# d) the same as above, post converting the array into ASCII characters and sorting alphabetically.
# The four parts should form a single string, each part separated by a hyphen: '-'
# example format of solution: 'asdf-tyui-ujng-wedg'

l = ['et', 3, 'at','ziggy', 1, 2,  'concat', 4]

a = []
b = []





y = 0
while y != 4:
    print(l.pop())
    y += 1

print(l)









































































# def capitalize(string, sub_string):
#     ## Convert sub_string to  tuple ##
#     sub_string_to_list = []
#     sub_string_to_list[len(sub_string_to_list):] = sub_string
#     list_to_tuple = tuple(sub_string_to_list)
#
#
#     # if sub_string in string:
#     #     print('True')
#     # else:
#     #     print('False')
#     # print(string.count(sub_string))
#     import itertools
#     a = itertools.combinations_with_replacement(string, len(sub_string))
#     b = list(a)
#     print(b)
#     set_a_counting_variable = 0
#     for each_tuple in  b:
#         if each_tuple == list_to_tuple:
#             set_a_counting_variable += 1
#     print(set_a_counting_variable)
#
# capitalize('ABCDCDC', 'CDC')










