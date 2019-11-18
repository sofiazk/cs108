# file name: a06_printing_shapes.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: printing patterns with the for loop, raging rabbits revisited.

def print_rect(ch, width, height):
     """prints out the character ch in the shape of a rectangle"""
     for g in range(height):
          print(ch * width)
        
def print_upper_left_triangle(ch, height):
     """character ch in the shape of an upper left triangle of size height"""
     for g in range(height, 0, -1):
          print(ch * g)

def print_upper_right_triangle(ch, height):
     """ prints out the character ch in the shape of an upper
     right triangle of size height"""
     for g in range(height, 0, -1):
          print(" " * (height - g) + ch * g)
        
def print_lower_left_triangle(ch, height):
     """that prints out the character ch in the shape of a lower left triangle of size height"""
     for g in range(height + 1):
          print(ch * g)
        
def print_lower_right_triangle(ch, height):
     """prints out the character ch in the shape of a lower right triangle of size height"""
     for g in range(height + 1):
          print(" " * (height - g) + ch * g)
        
def print_pyramid(ch, height):
     """prints out the character ch in the shape of a pyramid of size height"""
     for g in range(0, height):
          print(' '*(height - g), ch*((g+1)*2 -1))
        
def print_diamond(ch, height):
     """prints out the character ch in the shape of a diamond of size height"""
     for g in range(int(height/2 + 1)):
          print(" "*(height - g), ch*(g*2+1))
     for g in range(int((height - 2)/2), -1, -1):
          print(" "*(height - g), ch*(g*2+1))




if __name__ == '__main__':
    print_rect('*', 7, 5)
    print("    ")
    print_upper_left_triangle('*', 7)
    print("    ")
    print_upper_right_triangle('*', 7)
    print("    ")
    print_lower_left_triangle('*', 5)
