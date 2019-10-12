# Print vowels in the the order in which they appear in the string, prior to consonants

def vowels_and_consonants (s):
    vowels = 'aeiou'
    vowels_s = consonants_s = ''

    for letter in s:
        if letter in vowels:
            letter += vowels_s
            print(letter)

        else:
            consonants_s += letter

    for consonant in consonants_s:
        print(consonant)


vowels_and_consonants('javascriptloops')









