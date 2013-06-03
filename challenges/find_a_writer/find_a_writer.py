"""
Solution Accepted
Fri 17 May 2013

"""
import sys

test_cases = open('input.txt', 'r')

for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

    string_fragments = test.partition('|')
    author_name = []

    for character_id in string_fragments[2].split():
        author_name.append(string_fragments[0][int(character_id)-1])

    print "".join(author_name)

test_cases.close()