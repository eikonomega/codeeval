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
    string_fragments = test.split()

    # If string length isn't 0.
    if string_fragments:

        # Reverse the string.
        reversed_string = string_fragments[::-1]

        # Print the mth_to_last_element
        try:
            print reversed_string[int(reversed_string[0])]

        except IndexError:  # Ignore invalid element references.
            pass

test_cases.close()