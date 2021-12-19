import os
import sys

from pprint import pprint

def parse_input_file(file_in: str) -> list:
    '''
    Parses the input file into...
    Input Example:
    '''
    with open(file_in, 'r') as input_fh:
        input_lines = input_fh.readlines()

    #return list(map(int, input_lines[0].split(',')))


if __name__ == '__main__':
    ##########
    # Part 1 #
    ##########
    print('#'*25)
    print('Part 1: ')
    print('#'*25)

    parsed_input = parse_input_file(sys.argv[1])


#    ##########
#    # Part 2 #
#    ##########
#    print('#'*25)
#    print("Part 2: ")
#    print('#'*25)
#
#    parsed_input = parse_input_file(sys.argv[1])
