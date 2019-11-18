# file:  a04_raging_rabbits.py
# author: Sofia Kurd (sofiak@bu.edu)
# description:

from a04_artillery_games import calculate_projectile_distance
from a04_artillery_games import calculate_launch_angle
import random
import math

def raging_rabbits():
    print("Welcome to Raging Rabbits!")
    initial_velocity = float(input("Enter your cannon's initial launch velocity(in m/s): "))
    
    minimum_distance = calculate_projectile_distance(10, initial_velocity)
    maximum_distance = calculate_projectile_distance(45, initial_velocity)
    print("At an initial launch velocity of ", initial_velocity,
          " meters/second your cannon can hit a target between: %.2f " % minimum_distance, " and %.2f" % maximum_distance, " meters.")

    random_distance = random.randint(int(minimum_distance), int(maximum_distance))
    print("Your target is located at", random_distance, "meters.")

    launch_angle = float(input("Enter the launch angle in degrees: "))
    travel_amt = calculate_projectile_distance((launch_angle), (initial_velocity))
    print("Your projectile travelled %.2f " % travel_amt, "meters.")
    meters_from_target = random_distance - travel_amt
    print("Your shot was %.2f " % meters_from_target, "meters from the target.")

if __name__ == '__main__':
    raging_rabbits()
