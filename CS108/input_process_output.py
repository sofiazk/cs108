# file: input_process_output.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: Demonstrate the input - process - output design pattern


def convert_to_meters(feet, inches):
    """Convert a measurement in ft and inches from standard to metric format."""

    # combine feet and inches to get total amt in inches
    total_inches = 12 * feet + inches

    # convert inches to meters:
    meters = total_inches * 0.0254

    # return the amount in meters
    return meters

# our main program here:
if __name__ == '__main__':

    # collect the inputs: feet and inches
    print("Please enter your height in feet and inches:")
    feet = int(input("Feet: "))
    inches = int(input("Inches: "))
    # apply a process
    meters = convert_to_meters(feet, inches)

    # print an output to the user
    print("Your height is " + str(meters) + " meters.")
