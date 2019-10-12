
if __name__ == '__main__':
    s = 'BANANA'

    kevin = 0
    stuart = 0
    vowels = 'AEIOU'

    for i in range(len(s)):
        if s[i] in vowels:
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if kevin == stuart:
        print('Draw')

    elif kevin < stuart:
        print('Stuart ' + str(stuart))
    else:
        print('Kevin ' + str(kevin))