"""
Accepted on May 18, 2013

"""
import sys

test_cases = open('input.txt', 'r')

# Create list to hold identified prime numbers.
# Accept that 2 is the first prime number.
prime_numbers = ['2']

for test in test_cases:

    # If test is not a valid integer, skip fileline.
    try:
        int(test)
    except ValueError:
        continue

    # Get the great prime number already identified.
    # This will keep us from considering these numbers over again.
    highest_identified_prime = int(prime_numbers[-1])

    # For each test, iterate over the integers < test and
    # evaluate whether each number in range is a prime number...
    for possible_prime in range(highest_identified_prime + 1, int(test)):
        number_is_prime = True

        # By attempting to divide it by all integers that come before it.
        for divisor in range(2, possible_prime):
            if possible_prime % divisor == 0:
                number_is_prime = False

        if number_is_prime:
            prime_numbers.append(str(possible_prime))

    print ",".join(prime_numbers)

test_cases.close()