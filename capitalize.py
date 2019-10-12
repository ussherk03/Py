#Captalize the first letter of a word(s) in a string separated by spaces from each other.#
# a = 'ussher kingsley' ==> 'Ussher Kingsley', b = 'look unto him' ==> 'Look Unto Him'

def capitalize_alt(u):
    print(u.title())

def capitalize(s):
    s.split()
    l = s.split(' ')

    a = []

    for item in l:
        if item.islower():
            a.append(item.capitalize() + ' ')
        elif item.istitle():
            a.append(item.lower() + ' ')
        elif item.capitalize():
            a.append(item.lower() + ' ')
        else:
            a.append(item.capitalize() + ' ')

    p = ''.join(a)

    return p

print(capitalize('hello world'))
print(capitalize('under pressure By queen FT. david bOwie'))
capitalize_alt('hello world')







