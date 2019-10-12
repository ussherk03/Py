
## A leap year is divisible by 4 as much as 400 ##

def is_it_a_leap_year(year):
    is_leap = False
    if (year % 100 != 0 or year % 400 == 0) and year % 400 == 0:
        is_leap = True
        print(is_leap)
    else:
        print(is_leap)

is_it_a_leap_year(1992)



## A leap year is divisible by 4 as much as 400 ## 1992 problem