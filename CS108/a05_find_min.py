# file name: a05_find_min.py
# author: Sofia Kurd (sofiak@bu.edu)
# description:

def my_min(a, b):
    if a > b:
        return b
    elif b > a:
        return a

def find_min(a, b, c):
    if a < b and a < c:
        return a
    elif b <= a and b <= c:
        return b
    elif c <= a and c <= b:
        return c
    else:
        return a


if __name__ == '__main__':
    print('my_min(1,2)', my_min(1,2))
    print('my_min(2,1)', my_min(2,1))
    print('find_min(3,4,7)', find_min(3,4,7))
    print('find_min(400,2,-1)', find_min(400,2,-1))
