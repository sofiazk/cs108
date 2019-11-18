# file name: a09_list_comprehensions.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: Uses list comprehensions to return string results

def triple(values):
    '''Processes a sequence of values(numeric or string), and returns a list
    containing the triple of each original value'''
    result = []

    for x in values:
        result.append(x * 3)
    return result

def get_powers(b,n):
    '''Returns the first n powers of base b. Use built in function range to
    create app. sequence over which to run list comprehension.'''
    result = []
    for exponent in range(n+1):
        result.append(b**exponent)
    return result

def get_factors(n):
    '''returns a list containing all of the divisors of integer n'''
    factors = []

    for x in range(n):
        if n % x == 0:
            result.append(x % n)
    return factors
    

if __name__ == '__main__':

    print(triple([1, 2, 3]))
    print(triple(['a','b','c']))
    print(get_powers(2,10))
    print(get_powers(3,8))
    print(get_factors(10))
