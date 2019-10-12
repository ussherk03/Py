
import datetime


if __name__ == '__main__':
    n = input() # n must always be even
    date = []
    # Convert to datetime
    for _ in range(int(n)):
        date.append(datetime.datetime.strptime(input(), '%d %b %Y'))

    # Datetime values
    diff1 = round(abs((date[0] - date[1]).total_seconds()))
    diff2 = round(abs((date[2] - date[3]).total_seconds()))
    print(diff1, diff2)


































