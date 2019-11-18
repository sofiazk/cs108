# file: a08_string_puzzles.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: string processing puzzles 

def reverse(s):
    '''returns a version of string s backwards'''
    reverse_s = ""
    for x in range(len(s)):
        reverse_s += s[-1-x]
    return(reverse_s)


def every_other(s):
    '''returns a version of string s with every other letter'''
    str_every_other = ""
    for x in range(len(s)):
        if x%2 == 0:
            str_every_other += s[x]
    return(str_every_other)


def outside_chars(s, n):
    '''returns a version of s with only the first and last n characters'''
    last = ""
    first = s[0:n]
    for x in range(n):
        last += s[-1-x]
        last = reverse(last)
    return(first + last)

def triple_outsides(s):
    '''takes a string s and returns a version of that string with other 1st
    three characters from beginning and end of s triples, and rest in the middle''' 
    last = ""
    first = s[0]
    for x in range(len(s)):
        last += s[-1-x]
        return(str(first) * 3) + (str(last) * 3)

def swap_halves(s):
    '''takes a string s and returns a new string in which the 2 halves of the string
    have been swapped'''
    half1 = ""
    half2 = int(len(s)/2)
    return(s[half2:] + s[:half2])

def slice_middle(s):
    '''takes a string s, and returns a substring which is the middle half of the string'''
    q1 = ""

if __name__ == '__main__':
    print(reverse("bagel"))
    print(every_other("bagel"))
    print(outside_chars("yesterday", 2))
    print(triple_outsides("cayenne"))
    print(swap_halves("good day sunshine "))
    print(slice_middle("you know my name"))
