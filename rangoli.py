
if __name__ == '__main__':
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    size = 3
    zero_based = size - 1

    # Slice from a to c inclusive and then from c to b inclusive
    q = alpha[0: 3]
    r = [(i + '-') for i in q]
    t = list(reversed(r))
    t.pop()
    t_ = t
    print(q) # string sliced for size = 3
    print(r) # elements hyphenated
    print(t_) # elements to stand behind [elements of r]


    center_list = t_ + r # join the t_ and r to form
    center = ''.join(center_list)
    print(center.center(11, '-'))
    for i in range(len(center_list)):
        if i == round((len(center_list) - 1)/ 2):
            del center_list[i]


    print(center_list)




    print(center_list)













