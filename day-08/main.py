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


def infer_wiring(patterns: list) -> list:
    '''
    Given a list of signal patterns, determine what the wiring for the seven
    segment display should be in a fashion similar to what is outlined in the
    examples. In this case, it would look like this with the numbers indicating
    the index of list being returned.

     0000
    1    2
    1    2
     3333
    4    5
    4    5
     6666
    '''
    wiring = ['.'] * 7
    # Start by finding any oddballs and identifying the segments they use
    one = sorted(find_by_len(patterns, 2))
    seven = sorted(find_by_len(patterns, 3))
    four = sorted(find_by_len(patterns, 4))
    eight = sorted(find_by_len(patterns, 7))

    # First, the digit one. It is possible we swap the top and bottom.
    # I think I'll just need to circle back after other infering is complete
    # to figure out the top and bottom
    # use 6 to determine what the top or the bottom is, six will only contain the bottom
    wiring[2] = one[0][0]
    wiring[5] = one[0][1]

    # Because there is only a one segment difference between one and seven,
    # we'll do that next, just exclude the two segments we already have
    # mapped
    wiring[0] = list(set(seven[0]) - set(one[0]))[0]

    # After this, we can focus on three because it's the only len(5) digit
    # that has both segments 2 and 5 lit.
    three = sorted(list(filter(lambda x: (wiring[2] in x and wiring[5] in x), find_by_len(patterns, 5))))
    wiring[6] = list(set(three[0]) - (set(seven[0]) | set(four[0])))[0]
    wiring[3] = list(set(three[0]) - (set(one[0]) | set(seven[0]) | set(wiring[6])))[0]

    # Use the last segment of four to mark segment 1
    wiring[1] = list(set(four[0]) - set(three[0]))[0]

    # Use eight - (four + three) to isolate segment 4
    wiring[4] = list(set(eight[0]) - (set(four[0]) | set(three[0])))[0]

    # Find a five to confirm segments 2 and 5
    potential_fives = sorted(find_by_len(patterns, 5))
    # Filter out threes
    potential_fives = list(filter(lambda x: not (wiring[2] in x and wiring[5] in x), potential_fives))
    # We can be confident in our assessment of four, which bolsters segment 1
    # which can eliminate all twos
    five = list(filter(lambda x: wiring[1] in x, potential_fives))
    segment_2 = list(set(four[0]) - set(five[0]))[0]
    if wiring[2] != segment_2:
        wiring[5] = wiring[2]
        wiring[2] = segment_2

    return wiring

def convert_segment_to_int(segment: list, segment_map: list) -> int:
    '''
    Given a list of segment values and a map of letters to segment locations,
    return an integer represented by the segment input.
    '''
    segment_mappings = [
        sorted([x for (i, x) in enumerate(segment_map) if i in (0,1,2,4,5,6)]),
        sorted([x for (i, x) in enumerate(segment_map) if i in (2,5)]),
        sorted([x for (i, x) in enumerate(segment_map) if i in (0,2,3,4,6)]),
        sorted([x for (i, x) in enumerate(segment_map) if i in (0,2,3,5,6)]),
        sorted([x for (i, x) in enumerate(segment_map) if i in (1,2,3,5)]),
        sorted([x for (i, x) in enumerate(segment_map) if i in (0,1,3,5,6)]),
        sorted([x for (i, x) in enumerate(segment_map) if i in (0,1,3,4,5,6)]),
        sorted([x for (i, x) in enumerate(segment_map) if i in (0,2,5)]),
        sorted([x for (i, x) in enumerate(segment_map) if i in (0,1,2,3,4,5,6)]),
        sorted([x for (i, x) in enumerate(segment_map) if i in (0,1,2,3,5,6)]),
    ]
    value = []
    for digit in segment:
        value.append(str(segment_mappings.index(sorted(digit))))
    return int(''.join(value))

def find_by_len(patterns: list, length: int) -> list:
    '''
    Given a list of inputs, return the patterns representing characters with
    segment lengths matching length.
    '''
    return list(filter(lambda x: (len(x) == length), patterns))

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

    ##########
    # Part 2 #
    ##########
    print('#'*25)
    print("Part 2: ")
    print('#'*25)

    parsed_input = parse_input_file(sys.argv[1])
    total_value = 0
    for signal, output in parsed_input:
        #print('-'*20)
        wiring = infer_wiring(signal)
#        print(f''' Wiring diagram:
#
#     {wiring[0]*4}
#    {wiring[1]}    {wiring[2]}
#    {wiring[1]}    {wiring[2]}
#     {wiring[3]*4}
#    {wiring[4]}    {wiring[5]}
#    {wiring[4]}    {wiring[5]}
#     {wiring[6]*4}
# ''')
        output_value = convert_segment_to_int(output, wiring)
        #print(f'Signal value: {output_value}')
        total_value += output_value
    print(f'Total of all output values: {total_value}')

