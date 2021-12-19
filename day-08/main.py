import os
import sys

from pprint import pprint

def parse_input_file(file_in: str) -> (list, list):
    '''
    Parses the input file into a pair of lists corresponding to the signal pattern
    and the output value
    Input Example:
        be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
        edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
        fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
    '''
    with open(file_in, 'r') as input_fh:
        input_lines = input_fh.readlines()

    signal_patterns = [x.split('|')[0].split() for x in input_lines]
    output_values = [x.split('|')[1].split() for x in input_lines]
    return list(zip(signal_patterns, output_values))


def find_oddballs(patterns: list) -> list:
    '''
    Given a list of inputs (can be signal patterns or output values), return
    the patterns representing characters with unique segment lengths. In this
    case, we're talking about the digits 1, 4, 7, and 8.
    '''
    return list(filter(lambda x: (len(x) in (2, 3, 4, 7)), patterns))

if __name__ == '__main__':
    ##########
    # Part 1 #
    ##########
    print('#'*25)
    print('Part 1: segmented sadness')
    print('#'*25)

    parsed_input = parse_input_file(sys.argv[1])
#    for _, output in parsed_input:
#        print('-'*20)
#        pprint(output)
#        pprint(find_oddballs(output))
    all_oddballs = sum(map(len, map(find_oddballs, [out for (_,out) in parsed_input])))
    print(f'{all_oddballs} segments with unique lengths')

#    ##########
#    # Part 2 #
#    ##########
#    print('#'*25)
#    print("Part 2: ")
#    print('#'*25)
#
#    parsed_input = parse_input_file(sys.argv[1])
