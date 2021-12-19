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

def age_lanternfish(ages: list, goal_gen, cur_gen: int) -> list:
    '''
    Given a list of lanternfish ages, returns their ages after one year, 
    including any new lanternfish that have been born.
    '''
    if cur_gen <= goal_gen:
        for age_idx, age in enumerate(ages):
            if age == 0:
                ages[age_idx] = 6
                ages.append(9)
            else:
                ages[age_idx] -= 1
        return age_lanternfish(ages, goal_gen, cur_gen+1)
    return len(ages)

if __name__ == '__main__':
    ##########
    # Part 1 #
    ##########
    print('#'*25)
    print('Part 1: kind of exponential growth')
    print('#'*25)

    lanternfish_ages = parse_input_file(sys.argv[1])
    lanternfish_ages = age_lanternfish(lanternfish_ages, 80, 1)
    print(f'Generation {80}: {lanternfish_ages}')
        #pprint(lanternfish_ages)


    ##########
    # Part 2 #
    ##########
    print('#'*25)
    print("Part 2: but for real this time")
    print('#'*25)

    lanternfish_ages = parse_input_file(sys.argv[1])
    ages = [0] * 9

    # Populate the initial set of ages
    for age in lanternfish_ages:
        ages[age] += 1

    for gen in range(1, 257):
        new_age = [0] * 9
        for age_idx, age in enumerate(ages):
            if age_idx == 0:
                new_age[6] += ages[0]
                new_age[8] += ages[0]
            else:
                new_age[age_idx-1] += ages[age_idx]
        ages = new_age

        #print(f'generation: {gen} :: {sum(ages)}')
    print(f'generation: {gen} :: {sum(ages)}')
