import os
import sys

from pprint import pprint

def parse_input_file(file_in: str) -> list:
    '''
    Parses the input file into a list of ints
    Input Example:
    16,1,2,0,4,2,7,1,2,14
    '''
    with open(file_in, 'r') as input_fh:
        input_lines = input_fh.readlines()

    return list(map(int, input_lines[0].split(',')))


if __name__ == '__main__':
    ##########
    # Part 1 #
    ##########
    print('#'*25)
    print('Part 1: ')
    print('#'*25)

    crab_positions = parse_input_file(sys.argv[1])
    # Find the average distance to every given position?
    # maybe do a population distribution combined with a mean and mode?
    # This kind of feels like a sorting problem, but my intuition is telling me to not go that route
    # Also kind of feels like a matrix kind of thing so I'm going to go naive first
    total_distance = []
    total_gas = []
    for pos in range(0, max(crab_positions)):
        total_distance.append([abs(x - pos) for x in crab_positions])
        total_gas.append(sum([gas for gas in total_distance[pos]]))
        #print(f'pos: {pos} - gas {total_gas[pos]}')

    print(f'Cheapest pos: {total_gas.index(min(total_gas))} for {min(total_gas)}')



#    ##########
#    # Part 2 #
#    ##########
#    print('#'*25)
#    print("Part 2: ")
#    print('#'*25)
