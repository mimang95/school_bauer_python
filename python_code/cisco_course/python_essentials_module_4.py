'''
# 4.3.1.6
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# 4.3.1.7
def days_in_month(year, month):
    if(month in [1, 3, 5, 7, 8, 10, 12]):
        return 31
    elif (month in [4, 6, 9, 11]):
        return 30
    else:
        if(is_leap_year(year) == True):
            return 29
        else:
            return 28
# 4.3.1.8
def day_of_year(year, month, day):
    days = 0
    for i in range(1, month):
        days += days_in_month(year, i)
    days += day
    return days

# 4.3.1.9 prime numbers
def is_prime(num):
    for i in range(2, num - 1):
        if(num % i == 0):
            return False
        else:
            continue
    return True
'''

