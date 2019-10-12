
def count_letters_and_integers():
    a = input('Enter a string: ')
    b = c = 0
    for x in a:
        if a.isalpha():
           b += 1
        elif a.isnumeric():
           c += 1
    print('LETTERS --->', b, '\n NUMBERS --->', c)

count_letters_and_integers()
