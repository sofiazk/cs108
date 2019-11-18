#
# file: This file is a program which determines the most efficient way of giving
# change (which uses the fewest coins).
#
# author: Sofia Kurd
# email: sofiak@bu.edu

# To make the autograder script work, you will need to follow these constraints:
# * You must have variables named price, change, quarters, dimes, nickels,
#   and pennies. You may include any additional variables you choose.
# * In your finished code, the only place in your file that may contain print( )
#   statements is inside the if __name__ == '__main__': section at the bottom of
#   the file (see starter code) – otherwise the autograder script will fail.
#   You may use print statements elsewhere in your code while you are developing
#   and testing, but you must comment out those print statements before submission. 
#   The reason for this will be explained further next class.

# once you have a working solution, you should change this line to test other 
# starting values, e.g., 68 cents, 69 cents, etc. to ensure that your calculations 
# work for each value.
price = 68
change1 = x
change2 = y
change3 = z
quarters = 25
dimes = 10
nickels = 5
pennies = 1
__main__ = a

# do all of your computations here:
price // quarters = x
(price - quarters*x)//dimes = y
(price - quarters*x - dimes*y)//nickels = z
(price - quarters*x - dimes*y - nickels*z)//pennies = a
__main__ = x+y+z+a



if __name__ == '__main__':

    # put all print statements in this section, indented by one tab, e.g., :
    print('The price is', price,'cents.' )  
    
    
