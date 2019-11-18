# file: a07_accumulator.py
# author: Sofia Kurd (sofiak@bu.edu)
# description:

def sum_of_range(start, stop, skip):
    '''Calculates and returns the sum of the numbers produced by the
    range function'''
    sum = 0
    for i in range(start, stop, skip):
        sum += i
    print(sum)
    
def replace(s, old_ch, new_ch):
    '''Processes the string s and replaces all occurrences of char old_ch with
    new_ch'''
    result = ""
    for old_ch in s:
            s.split(old_ch)
            new_ch.join(new_ch)
    return(s + new_ch)

print(replace("chocolate", "o", "a"))

def calculate_average():
    '''Collects input from keyboard, calculates and prints out avg of inputs'''
    n = int(input("How many observations do you have? "))
    sum = 0
    for i in range(0, n):
        sum += int(input("Enter next value: "))

    print("The average is " + str(sum/n) + ".")
    
sum_of_range(1, 5, 1)
calculate_average()

    
    

