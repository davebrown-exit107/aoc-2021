import os
import sys

from pprint import pprint

def parse_input_file(file_in: str) -> list:
    '''
    Parses the input file into a matrix, mapping the risk at each point.
    Input Example:
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678
    '''
    with open(file_in, 'r') as input_fh:
        input_lines = input_fh.readlines()

    risk_map = []
    for line in input_lines:
        risk_map.append([int(x) for x in line.strip()])

    return risk_map


if __name__ == '__main__':
    ##########
    # Part 1 #
    ##########
    print('#'*25)
    print('Part 1: ')
    print('#'*25)

    risk_map = parse_input_file(sys.argv[1])
    pprint(risk_map)


#    ##########
#    # Part 2 #
#    ##########
#    print('#'*25)
#    print("Part 2: ")
#    print('#'*25)
#
#    parsed_input = parse_input_file(sys.argv[1])
