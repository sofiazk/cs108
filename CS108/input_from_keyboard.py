# file: input_from_keyboard.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: demonstrate taking inputs from the input_from_keyboard

def do_greeting():
    """Take some inputs from the user, and display a welcome message"""

    # prompt the user tp enter their name
    name = input("What is your name? ")

    # display welcome message with name
    # print("hello, " name) # note: 2 spaces in output
    # print ("Hello,", name, ".")

    print ("Hello,", + name + ".") # + operator does concantenation (joining
    # strings together)
    # prompt the user to enter a number

    age = int(input("What is your age?")) # treat this input as an integer
    # use the number in a calculation
    next_age = age + 1
    # display the result of calculation
    print("On your next birthday, you will be " + str(next_age) + " years old.")
# some test code:
if __name__ == '__main__':

    do_greeting() # call our function
