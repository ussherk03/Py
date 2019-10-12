import re


# ------------Test-cases for input----------
# learn.point@learningpoint.net
# learnpoint@learningpoint.net
# learnpoint@learningpoint.net1
#
# its@gmail.com1
# mike13445@yahoomail9.server
# rase23@ha_ch.com
# daniyal@gmail.coma
# thatisit@thatisit

def filter_valid_emails ( ):
    n = int(input())
    emails = []

    for _ in range(n):
        emails.append(input())

    filtered_emails = []

    for each_string in emails:
        # If email contains a dot
        if '.' in each_string:
            position_of_dot = each_string.index('.')

            extension = each_string[(position_of_dot + 1):]

            model = re.compile('[a-zA-Z0-9_-]*@[a-z0-]*\.[a-z]{3}') # Sets the model of every valid email address

            m = model.match(each_string)

            # In case the email matches the model while length of extension(eg. com)  is three
            if m is not None and len(extension) == 3:
                filtered_emails.append(each_string)

            else:
                pass

        # deletes each email which has no dot;
        else:
            del each_string



    return sorted(filtered_emails)

print(filter_valid_emails())




















# Alternative Solution **

'''def fun(s):
    # return True if s is a valid email, else return False
    import re

    boolean = False

    model = re.compile('\w[a-zA-Z0-9_-]*@[a-z0-9]*\.[a-z]{3}')

    m = model.match(s)

    if m is not None:
        boolean = True

        return boolean

    else:
        return boolean



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)

'''








