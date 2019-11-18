# file: a10_date.py
# starter code by Aaron Stevens (azs@bu.edu)
# ## author: Sofia Kurd (sofiak@bu.edu)
#
# description: implementation of a Date class to represent a calendar date
#

##########################################################################################
class Date:

    # Date.__init__(self,month,day,year)

    ##########################################################################################
    def __init__(self, month, day, year):
        '''Initialize this Date object.'''

        self.month = month
        self.day = day
        self.year = year

    ##########################################################################################
    def __repr__(self):
        '''Return a beautifully-formatted string representation
        of this date as YY/MM/DD.'''

        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        '''returns true if the called object is in a leap year, and False
        otherwise'''

        if not self.year % 4 == 0:
            return False
        elif self.year < 0:
            return False
        if self.year % 100 == 0 and not self.year % 400 == 0:
            return False
        else:
            return True


# sofia_kurd_birthday = Date(5,11,1999)
# sofia_kurd_birthday.is_leap_year()
# sofia_kurd_birthday.__repr__()

    def is_valid_date(self):
        '''Returns true if object is a valid date, and false otherwise'''


        days_30 = [4, 6, 9, 11]
        if self.day > 31:
            return False
        elif self.month > 12:
            return False
        elif self.month == 2 and self.is_leap_year() and self.day > 29:
            return False
        elif self.month == 2 and not self.is_leap_year() and self.day > 28:
            return False
        elif self.month in days_30 and self.day > 30:
            return False
        return True


    def add_one_day(self):
        '''Changes the called object so that it represents one calendar day
        after the date it originally represented'''


        days_30 = [4, 6, 9, 11]
        days_31 = [1, 3, 5, 7, 8, 10, 12]
        # handles next pour-over for days_30
        if self.month in days_30:
            if self.day == 30:
                self.day = 1
                self.month += 1
        # handles next pour-over for days_31
        if self.month in days_31:
            if self.day == 31:
                self.day = 1
                self.month += 1

        if self.month == 2:
            if self.day == 28 and self.is_leap_year():
                self.month = 2
                self.day = 29
            elif self.day == 28 and not self.is_leap_year():
                self.month = 3
                self.day = 1
        else:
            self.day += 1


    def rem_one_day(self):
        '''Changes the called object so that it represents one
        calendar day before the date that it originally represented'''


        days_30 = [4, 6, 9, 11]
        days_31 = [1, 3, 5, 7, 8, 10, 12]
        # handles next pour-over for days_30
        if self.month in days_30:
            if self.day == 30:
                self.day = 1
                self.month -= 1
        # handles next pour-over for days_31
        if self.month in days_31:
            if self.day == 31:
                self.day = 1
                self.month -= 1
        if self.month == 2:
            if self.day == 28 and self.is_leap_year():
                self.month = 2
                self.day = 29
            elif self.day == 28 and not self.is_leap_year():
                self.month = 3
                self.day = 1
        else:
            self.day -= 1


    def add_n_days(self, n):
        '''Changes the calling object so that it represents n calendar days after
        the date it was originally represented'''


        for x in range(0, n):
            print(self)
            self.add_one_day()
        print(self)


    def rem_n_days(self, n):
        '''Changes the calling object so that it represents n calendar days before
        the date it originally represented'''


        for x in range(0, n):
            print(self)
            self.rem_one_day()
        print(self)


    def is_before(self, other):
        '''returns True if the called object represents a calendar date that
        occurs before the calendar date that is represented by other'''
        if other.year <= self.year:
            return False
        elif other.month <= self.month:
            return False
        elif other.day <= self.day:
            return False
        else:
            return True


   # file: a10_date.py
# starter code by Aaron Stevens (azs@bu.edu)
# ## author: Sofia Kurd (sofiak@bu.edu)
#
# description: implementation of a Date class to represent a calendar date
#

##########################################################################################
class Date:

    # Date.__init__(self,month,day,year)

    ##########################################################################################
    def __init__(self, month, day, year):
        '''Initialize this Date object.'''

        self.month = month
        self.day = day
        self.year = year

    ##########################################################################################
    def __repr__(self):
        '''Return a beautifully-formatted string representation
        of this date as YY/MM/DD.'''

        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        '''returns true if the called object is in a leap year, and False
        otherwise'''

        if not self.year % 4 == 0:
            return False
        elif self.year < 0:
            return False
        if self.year % 100 == 0 and not self.year % 400 == 0:
            return False
        else:
            return True


# sofia_kurd_birthday = Date(5,11,1999)
# sofia_kurd_birthday.is_leap_year()
# sofia_kurd_birthday.__repr__()

    def is_valid_date(self):
        '''Returns true if object is a valid date, and false otherwise'''


        days_30 = [4, 6, 9, 11]
        if self.day > 31:
            return False
        elif self.month > 12:
            return False
        elif self.month == 2 and self.is_leap_year() and self.day > 29:
            return False
        elif self.month == 2 and not self.is_leap_year() and self.day > 28:
            return False
        elif self.month in days_30 and self.day > 30:
            return False
        return True


    def add_one_day(self):
        '''Changes the called object so that it represents one calendar day
        after the date it originally represented'''


        days_30 = [4, 6, 9, 11]
        days_31 = [1, 3, 5, 7, 8, 10, 12]
        # handles next pour-over for days_30
        if self.month in days_30:
            if self.day == 30:
                self.day = 1
                self.month += 1
        # handles next pour-over for days_31
        if self.month in days_31:
            if self.day == 31:
                self.day = 1
                self.month += 1

        if self.month == 2:
            if self.day == 28 and self.is_leap_year():
                self.month = 2
                self.day = 29
            elif self.day == 28 and not self.is_leap_year():
                self.month = 3
                self.day = 1
        else:
            self.day += 1


    def rem_one_day(self):
        '''Changes the called object so that it represents one
        calendar day before the date that it originally represented'''


        days_30 = [4, 6, 9, 11]
        days_31 = [1, 3, 5, 7, 8, 10, 12]
        # handles next pour-over for days_30
        if self.month in days_30:
            if self.day == 30:
                self.day = 1
                self.month -= 1
        # handles next pour-over for days_31
        if self.month in days_31:
            if self.day == 31:
                self.day = 1
                self.month -= 1
        if self.month == 2:
            if self.day == 28 and self.is_leap_year():
                self.month = 2
                self.day = 29
            elif self.day == 28 and not self.is_leap_year():
                self.month = 3
                self.day = 1
        else:
            self.day -= 1


    def add_n_days(self, n):
        '''Changes the calling object so that it represents n calendar days after
        the date it was originally represented'''


        for x in range(0, n):
            print(self)
            self.add_one_day()
        print(self)


    def rem_n_days(self, n):
        '''Changes the calling object so that it represents n calendar days before
        the date it originally represented'''


        for x in range(0, n):
            print(self)
            self.rem_one_day()
        print(self)


    def is_before(self, other):
        '''returns True if the called object represents a calendar date that
        occurs before the calendar date that is represented by other'''
        if other.year <= self.year:
            return False
        elif other.month <= self.month:
            return False
        elif other.day <= self.day:
            return False
        else:
            return True


    def is_after(self, other):
        '''returns True if the calling object represent a calendar date that
        occurs after the calendar date that is represented by other'''
        if self.year <= other.year:
            return False
        elif self.month <= other.month:
            return False
        elif self.day <= other.day:
            return False
        else:
            return True


    # ##########################################################################################
    def __eq__(self, other):
        pass

    # '''Return True if both objects have the same month, day, year.'''
    #     return (self.year == other.year and
    #             self.month == other.month and
    #             self.day == other.day)

    ##########################################################################################
    def copy(self):
        '''Return a new Date object with the same
        data attributes as this Date.'''

        d = Date(self.month, self.day, self.year)
        return d


    ##########################################################################################
    ## TO DO: Write your other methods here...


    ##########################################################################################
    # A fully-implemented diff method is provided.
    # However, it will not work correctly until you
    # successfully implement the 'is_before', 'is_after',
    # 'add_one_day' and 'rem_one_day' methods.
    def diff(self, other):
        '''Return the number of days between self and other.'''

        # if the two dates are 'equal', return a difference of 0 days.
        if self == other:
            return 0

        # create a copy of other, so as not to change the actual other object
        other = other.copy()

        MAX_DIFF = 10000  # upper bounds for the for loop

        # if the other Date comes before this Date, we will count up
        # by adding one day at a time, until the two dates are 'equal'.
        if other.is_before(self):
            for i in range(1, MAX_DIFF):
                other.add_one_day()
                if other == self:
                    return i

        # if the other Date comes after this Date, we will count down
        # by removing one day at a time, until the two dates are 'equal'.
        elif other.is_after(self):
            for i in range(-1, -MAX_DIFF, -1):
                other.rem_one_day()
                if other == self:
                    return i

        print("Error in diff method! self=%s, other=%s, i=%d" % (self, other, i))
        return i  # Error case, should not happen

    def day_of_week(self):
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                     'Friday', 'Saturday', 'Sunday']
        return "Monday"

##########################################################################################
if __name__ == '__main__':
    ## TEST CODE HERE:
    # Use these date objects, or create your own.
    # Uncomment lines below as needed.
    # Test every method thoroughly!

    d = Date(8, 26, 2001)
    print('d =', d)

    m1 = Date(4, 20, 2020)
    print('m1 =', m1)
    m2 = Date(4, 20, 2020)
    print("m2 = ", m2)

    # test for equality, and print out the result of the expression
    print('m1 == m2 evalutes to', m1 == m2)

    # d1 = Date(10,11,2019)
    # d2 = Date(12,8,2019)
    # d3 = Date(10,28,2018)
    # print("d1 =", d1)
    # print("d2 =", d2)
    # print("d3 =", d3)

    ##print('d1.is_before(d2)', d1.is_before(d2))
    ##print('d2.is_before(d1)', d2.is_before(d1))
# print('d1.is_before(d3)', d1.is_before(d3))

# A fully-implemented diff method is provided.
# However, it will not work correctly until you
# successfully implement the 'is_before', 'is_after',
# 'add_one_day' and 'rem_one_day' methods.

# print('d1.diff(d2)',d1.diff(d2))
# print('d2.diff(d1)',d2.diff(d1))
# print('m.diff(d1)',m.diff(d1))
# print('d1.diff(d3)',d1.diff(d3))

def is_after(self, other):
        '''returns True if the calling object represent a calendar date that
        occurs after the calendar date that is represented by other'''
        if self.year <= other.year:
            return False
        elif self.month <= other.month:
            return False
        elif self.day <= other.day:
            return False
        else:
            return True

def day_of_week(self):
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                     'Friday', 'Saturday', 'Sunday']
        return "Monday"
    # ##########################################################################################
def __eq__(self, other):
    pass

    # '''Return True if both objects have the same month, day, year.'''
    #     return (self.year == other.year and
    #             self.month == other.month and
    #             self.day == other.day)

    ##########################################################################################
    def copy(self):
        '''Return a new Date object with the same
        data attributes as this Date.'''

        d = Date(self.month, self.day, self.year)
        return d


    ##########################################################################################
    ## TO DO: Write your other methods here...


    ##########################################################################################
    # A fully-implemented diff method is provided.
    # However, it will not work correctly until you
    # successfully implement the 'is_before', 'is_after',
    # 'add_one_day' and 'rem_one_day' methods.
    def diff(self, other):
        '''Return the number of days between self and other.'''

        # if the two dates are 'equal', return a difference of 0 days.
        if self == other:
            return 0

        # create a copy of other, so as not to change the actual other object
        other = other.copy()

        MAX_DIFF = 10000  # upper bounds for the for loop

        # if the other Date comes before this Date, we will count up
        # by adding one day at a time, until the two dates are 'equal'.
        if other.is_before(self):
            for i in range(1, MAX_DIFF):
                other.add_one_day()
                if other == self:
                    return i

        # if the other Date comes after this Date, we will count down
        # by removing one day at a time, until the two dates are 'equal'.
        elif other.is_after(self):
            for i in range(-1, -MAX_DIFF, -1):
                other.rem_one_day()
                if other == self:
                    return i

        print("Error in diff method! self=%s, other=%s, i=%d" % (self, other, i))
        return i  # Error case, should not happen


##########################################################################################
if __name__ == '__main__':
    ## TEST CODE HERE:
    # Use these date objects, or create your own.
    # Uncomment lines below as needed.
    # Test every method thoroughly!

    d = Date(8, 26, 2001)
    print('d =', d)

    m1 = Date(4, 20, 2020)
    print('m1 =', m1)
    m2 = Date(4, 20, 2020)
    print("m2 = ", m2)

    # test for equality, and print out the result of the expression
    print('m1 == m2 evalutes to', m1 == m2)

    # d1 = Date(10,11,2019)
    # d2 = Date(12,8,2019)
    # d3 = Date(10,28,2018)
    # print("d1 =", d1)
    # print("d2 =", d2)
    # print("d3 =", d3)

    ##print('d1.is_before(d2)', d1.is_before(d2))
    ##print('d2.is_before(d1)', d2.is_before(d1))
# print('d1.is_before(d3)', d1.is_before(d3))

# A fully-implemented diff method is provided.
# However, it will not work correctly until you
# successfully implement the 'is_before', 'is_after',
# 'add_one_day' and 'rem_one_day' methods.

# print('d1.diff(d2)',d1.diff(d2))
# print('d2.diff(d1)',d2.diff(d1))
# print('m.diff(d1)',m.diff(d1))
# print('d1.diff(d3)',d1.diff(d3))
