import datetime

def find_weekday ():
    try:
        string_input = input()

        string_date = datetime.datetime.strptime(string_input, '%d %m %Y')

        weekdays = {1: 'MONDAY', 2: 'TUESDAY', 3: 'WEDNESDAY', 4: 'THURSDAY', 5: 'FRIDAY', 6: 'SATURDAY', 7: 'SUNDAY'}

        s = string_date.isocalendar()
        day = s[2]

        return weekdays[day]

    except ValueError:
        return "You didn't input a valid date"



print(find_weekday())

