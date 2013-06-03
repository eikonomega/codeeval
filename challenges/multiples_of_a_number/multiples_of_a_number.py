"""
Solution Accepted
Mon 20 May 2013

"""
import sys

test_cases = open('input.txt', 'r')

for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

    # Split string into list.
    string_fragments = test.split(',')

    # For non-blank lines
    try:

        # Set initial values for comparison.
        number_to_beat = int(string_fragments[0])
        current_guess = int(string_fragments[1].rstrip("\n"))

        if current_guess >= number_to_beat:
            print current_guess
        else:
            while current_guess < number_to_beat:
                current_guess *= 2

            print current_guess

    # For blank lines
    except ValueError:
        pass

test_cases.close()