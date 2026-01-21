#!/usr/bin/env python3
# Created By: sarah OUAMOU
# Date: 12 31 2025
# This program calculates the average of 10 random numbers between 0 and 100.

import random


# Main function that controls program flow

def main():

# Initialize variables

# total sum of numbers

    total = 0

    # list to store numbers

    num_list = []

    num_min = 0

    num_max = 100

    max_number_of_num = 10

    # Loop to generate numbers

    for loop_counter in range(0, max_number_of_num):

        # Generate a random number

        rand_num = random.randint(num_min, num_max)

        # Add number to list

        num_list.append(rand_num)

        # Add number to total sum

        total += rand_num

        # Print each number as it's added (without f-string)

        print(str(rand_num) + " has been added to the sum.")

    # Calculate the average

    average = total / max_number_of_num