# file name: decisions.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: an example on decision statements with if/else logic in python
def print_letter_grade(grade):
    '''Print out a letter grade (A, B, C, ...) based on a numeric grade.'''
    if grade > 93:
        print("You get an A!")
    elif grade > 90:
        print("You get an A-.")
    elif grade > 88:
        print("You get a B+.")
    elif grade > 83:
        print("You get a B.")

    else:
        print("You get an F. Better luck next time.")
