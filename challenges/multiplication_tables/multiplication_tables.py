"""
Solution Accepted
May 29, 2013

"""
import sys

multiplication_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Add values to the multiplication table.
for iteration in range(1, 13):

    multiplication_table_line = ''

    # Iterate over multiplication_table to generate each results line.
    for number in multiplication_table:
        single_multiplied_value = str(iteration * number).rjust(4, ' ')
        multiplication_table_line += single_multiplied_value

    # Remove leading spaces from each line and print.
    print multiplication_table_line.lstrip()