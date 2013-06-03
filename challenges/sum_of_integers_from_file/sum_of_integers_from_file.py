"""
Solution Accepted
Mon 29 May 2013

"""
import sys

test_cases = open('input.txt', 'r')

# Set initial value of result variable.
cumulative_value_of_numbers = 0

for test in test_cases:
    # Strip newline characters from test
    test = test.rstrip("\n")
    
    # Add value of current line to cumulative_value_of_numbers
    cumulative_value_of_numbers += int(test)
    
print cumulative_value_of_numbers


test_cases.close()