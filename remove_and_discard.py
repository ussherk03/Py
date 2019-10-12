
if __name__ == '__main__':

    n = 9
    s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    num_of_commands = 1000

    for _ in range(num_of_commands):
        n = input()

        if n != 'exit':
            try:
                line = n.split()
                getattr(s, line[0])(*[int(line[1])] if len(line) > 1 else {})
                print(s)

            except TypeError:
                print('TypeError: Check Input')
                continue
            except KeyError and ValueError:
                print('KeyError: \'{0}\' cannot be found'.format(line[1]))
            except AttributeError:
                print('AttributeError: \'set\' object has no attribute \'{0}\''.format(line))

        else:
            break

    print('Set S:', s)

'''
--------Test Cases------
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
'''





