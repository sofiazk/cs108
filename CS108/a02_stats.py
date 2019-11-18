#
# File: a02_functions.py
# your name: Sofia Kurd
# your email: sofiak@bu.edu
#
#

# function 0: an example of funciton definition
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

def cube(x):
    """returns the cube of input given"""
    return x ** 3

# put your definitions for the remaining functions below

def slope(x1, y1, x2, y2):
    """returns the slope of the line formed by points (x1, y1) and (x2, y2)"""
    return (y2 - y1) / (x2 - x1)

def calc_sum(a, b, c, d, e):
    """returns the sum of 5 parameters"""
    return (a + b + c + d + e)

def calc_mean(a, b, c, d, e):
    """returns the average of 5 parameters"""
    return (a + b + c + d + e) / 5

def cylinder_volume(diameter, length):
    """returns the volume of a cylinder of a given diameter and length"""
    return 3.14159 * ((diameter/2) ** 2) * length

def calc_variance(a, b, c, d, e):
    """returns the variance of 5 parameters"""
    mean_of_num = (a + b + c + d + e) / 5
    return ( (a - mean_of_num)**2 + (b - mean_of_num)**2 + (c - mean_of_num)**2
    + (d - mean_of_num)**2 + (e - mean_of_num)**2) / 5

def calc_stdev(a, b, c, d, e):
    """returns the standard deviation of the 5 parameters"""
    mean_of_num = (a + b + c + d + e) / 5
    return (((a - mean_of_num)**2 + (b - mean_of_num)**2 + (c - mean_of_num)**2
    + (d - mean_of_num)**2 + (e - mean_of_num)**2) / 5) ** 0.5
    

# unit test code:
if __name__ == '__main__':

    # declare variables with which to test the functions
    a = 8
    b = 9
    c = 10
    d = 4
    e = 2

    x1 = 11
    x2 = 4
    y1 = 8
    y2 = 16

    diameter = 4
    length = 12

    # call the function to calculate the sum:
    slope = slope(x1, y1, x2, y2)
    calc_sum = calc_sum(a, b, c, d, e)
    calc_mean = calc_mean(a, b, c, d, e)
    cylinder_volume = cylinder_volume(diameter, length)
    calc_variance = calc_variance(a, b, c, d, e)
    calc_stdev = calc_stdev(a, b, c, d, e)

    # print the result
    print("The slope of the points is:", slope)
    print("The sum of observations is:", calc_sum)
    print("The mean of the numbers is:", calc_mean)
    print("The cylinder volume is:", cylinder_volume)
    print("The variance is:", calc_variance)
    print("The standard deviation is:", calc_stdev)
