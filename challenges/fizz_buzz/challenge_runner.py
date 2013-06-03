"""
Sample input

"""
import sys

test_cases = open('input.txt', 'r')

for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

    fizz_divisor, buzz_divisor, max_number = test.split()
    result = []
    for number in range(1, int(max_number)+1):
        if number % int(fizz_divisor) == 0:
            if number % int(buzz_divisor) == 0:
                result.append('FB')
            else:
                result.append('F')
        elif number % int(buzz_divisor) == 0:
            result.append('B')
        else:
            result.append(str(number))

    print " ".join(result)



test_cases.close()