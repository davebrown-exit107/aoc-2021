import os
import sys

from pprint import pprint

def parse_input_file(file_in: str) -> list:
    '''
    Parses the input file into a list of coordinates
    Input Example:
    '''
    with open(file_in, 'r') as input_fh:
        input_lines = input_fh.readlines()

    lanternfish_ages = list(map(int, input_lines[0].split(',')))
    return lanternfish_ages

def age_lanternfish(ages: list) -> list:
    '''
    Given a list of lanternfish ages, returns their ages after one year, 
    including any new lanternfish that have been born.
    '''
    for age_idx, age in enumerate(ages):
        if age == 0:
            ages[age_idx] = 6
            ages.append(9)
        else:
            ages[age_idx] -= 1
    return ages

if __name__ == '__main__':
    ##########
    # Part 1 #
    ##########
    print('#'*25)
    print('Part 1:')
    print('#'*25)

    lanternfish_ages = parse_input_file(sys.argv[1])
    for gen in range(1, 81):
        lanternfish_ages = age_lanternfish(lanternfish_ages)
        print(f'Generation {gen}: {len(lanternfish_ages)}')
        #pprint(lanternfish_ages)


#?    ##########
#?    # Part 2 #
#?    ##########
#?    print('#'*25)
#?    print("Part 2:")
#?    print('#'*25)
