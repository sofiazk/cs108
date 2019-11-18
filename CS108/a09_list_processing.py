# file name: a09_list_processing.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: Using list processing to write function that produces the required
            # result and returns a string result.

def my_sum(values):
    '''processes a list of numeric values and returns the sum of the values
        in that list'''
    result = 0

    for value in values:
        result += value
    return result

def my_max(values):
    '''processes a list of numeric values and return the maximum value from
        that list'''
    res = values[0]
    for i in values:
        if res < i:
            res = i
    return res

def powers(base, n):
    '''Builds and returns a list of all n powers of a given base'''
    powerslist = []

    for exponent in range(n+1):
        powerslist.append(base**exponent)
    return powerslist
    
def get_uniques(items):
    '''Takes as a parameter a list of items, and returns a list of only the
    unique items within the original list.'''

    uniques = []

    for x in items:
        if x not in uniques:
            uniques.append(x)
    return uniques


if __name__ == '__main__':
     values = [4, 7, 9, 2, 8, 5, 1, 6]
     print('my_sum(values)', my_sum(values))
     print('my_max(values)', my_max(values))
     print('powers(base, n)', powers(2, 10))
     items = ['to', 'be', 'or', 'not', 'to', 'be']
     print('get_uniques(items)', get_uniques(items))
