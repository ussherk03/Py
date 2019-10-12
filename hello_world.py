

def kill_vowels(phrase):
    null = ''
    bag = ''

	for letter in phrase:
		if letter in "AEIOUaeiou":
		    bag = bag + letter

	    else:
		    null = null + letter

	print(null)

kill_vowels('Roland Is A Good Lad')


def kill_vowels(string):
    vowels = 'AEIOUaeiou'
    harmless = ''
    unfit = ''
    for letter in string:
        if letter in vowels:
            unfit = unfit + letter
        else:
            harmless = harmless + letter
    print(harmless)


kill_vowels('Shut your beak!')
