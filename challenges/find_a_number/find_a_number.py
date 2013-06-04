"""
Solution Accepted???

"""
import sys

test_cases = open('input.txt', 'r')


def guess_my_number(bottom_of_guess_range, top_of_guess_range):
    """
    Find a number within a given range.  The number will be provided
    via a text file.

    While there are a number of ways that you could do this... I'm
    going to try to call this function recursively first and if that doesn't
    work I'll try a while loop.

    """

    current_guess = (top_of_guess_range + bottom_of_guess_range) / 2
    print 'My current_guess is {}'.format(current_guess)

    if current_guess == magic_number:
        print 'You found the secret number {}'.format(magic_number)
        return
    else:
        if current_guess > magic_number:
            # Set the new high_value to the current guess.
            top_of_guess_range = current_guess

        elif current_guess < magic_number:
            # Set the new low_value to the current guess.
            bottom_of_guess_range = current_guess

    # Recursively call the function.
    guess_my_number(bottom_of_guess_range, top_of_guess_range)

for test in test_cases:

    # Convert test case values into list
    test_case_values = test.split(',')

    # Test for integer values, otherwise skip loop iteration.
    try:
        low_value = int(test_case_values[0])
        high_value = int(test_case_values[1])
        magic_number = int(test_case_values[2])
    except (ValueError, IndexError):
        continue

    # Due to the algorithm being used, an edge case exists that will cause
    # an infinite recursion when the magic number is equal to the top of
    # the range.

    # There are a number of solutions for this, including:
    # 1. Guess the top of the range at the beginning of the exercise.
    # 2. Do the exercise with decimal numbers and allow when the guess is
    # within .5 of the magic number, round up the guess.
    # 3. Have the program remember the prior guess and increment guess by
    # one if it detects this edge case.

    # Since I need to get back to my day-job, I'm going to implement #1,
    # which seems the least elegant to me, but is the quickest.

    if magic_number == high_value:
        print 'The secret number {} is the top of the range.'.format(
            magic_number)
    else:
        guess_my_number(low_value, high_value)

test_cases.close()