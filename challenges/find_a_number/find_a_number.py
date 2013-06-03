"""
Solution Accepted???

"""
import sys

test_cases = open('input.txt', 'r')


def guess_my_number(bottom_of_guess_range, top_of_guess_range):
    """
    Find a number within a given range.  The number will be provided
    via a text file.

    Alternatively, min and max can also be provided by the program.

    While there are a number of ways that you could do this... I'm
    going to try to call this function recursively first and if that doesn't
    work I'll try a while loop.

    """

    current_guess = (top_of_guess_range + bottom_of_guess_range) / 2
    print current_guess

    if current_guess == magic_number:
        print 'You found the secret number %i' % magic_number
        return
    else:
        if current_guess > magic_number:
            # Set the new high_value to the current guess.
            top_of_guess_range = current_guess
            pass

        elif current_guess < magic_number:
            # Set the new low_value to the current guess.
            bottom_of_guess_range = current_guess
            pass

    guess_my_number(bottom_of_guess_range, top_of_guess_range)

for test in test_cases:

    # Set initial value of current_guess
    # current_guess = (max - min) / 2

    # Strip newline characters from test
    test = test.rstrip("\n")

    # Convert test case values into list
    test_case_values = test.split(',')

    # Test for integer values, otherwise skip loop iteration.
    try:
        low_value = int(test_case_values[0])
        high_value = int(test_case_values[1])
        magic_number = int(test_case_values[2])
    except (ValueError, IndexError):
        continue

    print low_value
    print high_value
    print magic_number

    guess_my_number(low_value, high_value)



test_cases.close()