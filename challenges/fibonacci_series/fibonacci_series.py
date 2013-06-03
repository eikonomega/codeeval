"""
Solution Accepted
Mon 21 May 2013

"""
import sys

test_cases = open('input.txt', 'r')

# Minimum starting values for program.
fibonacci_sequence = [0, 1]

# new_value = current_value + previous_value

for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

    # Strip newline characters from test
    test = test.rstrip("\n")

    fibonacci_sequence_number_to_retrieve = int(test)

    try:
        print fibonacci_sequence[fibonacci_sequence_number_to_retrieve]
    except IndexError:
        iterations = fibonacci_sequence_number_to_retrieve - \
                     fibonacci_sequence.__len__()

        for iteration in range(iterations + 1):
            fibonacci_sequence.append(
                fibonacci_sequence[-1] + fibonacci_sequence[-2]
            )

        print fibonacci_sequence[fibonacci_sequence_number_to_retrieve]



test_cases.close()