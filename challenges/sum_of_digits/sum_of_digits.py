"""
Solution Accepted
Mon 21 May 2013

"""
import sys

test_cases = open('input.txt', 'r')

for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

    # Strip newline characters from test
    test = test.rstrip("\n")

    # Set initial value of result variable.
    cumulative_value_of_numbers = 0

    # For each number with test case.
    for number in test:
        cumulative_value_of_numbers += int(number)

    print cumulative_value_of_numbers


test_cases.close()