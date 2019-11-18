# file: a04_artillery_games.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: Program that aims a cannon at a target using
                # physics/trigonometry calculations to determine the angle+velocity,
                # taking gravity into account
import math
import random

def calculate_projectile_distance(launch_angle, initial_velocity):
    """Computes and returns the distance (in meters) that a projective
    will travel, given its initial launch angle and velocity (meters/second)"""
    launch_radians = math.radians(launch_angle)
    distance = (float(initial_velocity ** 2)) / (9.8) * math.sin(launch_radians * 2)
    return distance

def calculate_launch_angle(distance, initial_velocity):
    """Computes + returns the required launch angle (in degrees) to hit a
    target at a known distance(meters) given its
    initial_velocity (meters/second)"""
    launch_angle = math.degrees((1 / 2) * (math.asin(9.8 * distance / (initial_velocity ** 2))))
    return launch_angle
