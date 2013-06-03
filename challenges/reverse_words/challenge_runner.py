"""
Solved on May 16, 2013

"""
import sys

test_cases = open('input.txt', 'r')

for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

    words = test.split()

    if words.__len__():
        words.reverse()
        print " ".join(words)

test_cases.close()