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
    print('Part 1: simple scuttlebutt')
    print('#'*25)

    crab_positions = parse_input_file(sys.argv[1])
    total_distance = []
    total_gas = []
    for pos in range(0, max(crab_positions)):
        total_distance.append([abs(x - pos) for x in crab_positions])
        total_gas.append(sum([gas for gas in total_distance[pos]]))
        #print(f'pos: {pos} - gas {total_gas[pos]}')

    print(f'Cheapest pos: {total_gas.index(min(total_gas))} for {min(total_gas)}')



    ##########
    # Part 2 #
    ##########
    print('#'*25)
    print("Part 2: cumulative catastrophe")
    print('#'*25)

    crab_positions = parse_input_file(sys.argv[1])
    total_distance = []
    total_gas = []
    for pos in range(0, max(crab_positions)):
        # Math works, we're just going to have to be creative again about getting at the solution
        # Just another big numbers problem...
        total_distance.append([sum([move for move in range(0, abs(pos - x)+1)]) for x in crab_positions])
        #print('#'*50)
        #print(f'position: {pos}')
        #pprint([[move for move in range(0, abs(pos - x))] for x in crab_positions])
        total_gas.append(sum([gas for gas in total_distance[pos]]))
        print(f'pos: {pos} - gas {total_gas[pos]}')

    print(f'Cheapest pos: {total_gas.index(min(total_gas))} for {min(total_gas)}')
    #pprint(total_distance[total_gas.index(min(total_gas))])
