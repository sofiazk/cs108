# file name: a05_valid_date.py
# author: Sofia Kurd (sofiak@bu.edu)
# description:
def is_valid_month(month):
    if month < 1:
        return False
    elif month > 12:
        return False
    else:
        return True
def is_leap_year(year):
    if not year % 4 == 0:
        return False
    elif year < 0:
        return False
    if year % 100 == 0 and not year % 400 == 0:
        return False
    else:
        return True
def is_valid_day_in_month(month,day,year):
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    if day > 31:
        return False
    elif month == 2 and is_leap_year(year) == True and day > 29:
        return False
    elif month == 2 and is_leap_year(year) == False and day > 28:
        return False
    if month in days_31 and day > 31:
        return False
    if month in days_30 and day > 30:
        return False
    else:
        return True
def get_month_name(number):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    return months[number - 1]


if __name__ == '__main__':
    print(is_valid_month(2))
    print(is_valid_month(13))
    print(is_valid_month(-13))
    
    print(is_leap_year(1912))
    print(is_leap_year(2000))
    print(is_leap_year(2200))
    print(is_leap_year(2016))

    print(is_valid_day_in_month(2,2,2022))
    print(get_month_name(3))
