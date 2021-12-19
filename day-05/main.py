import os
import sys

from pprint import pprint

def parse_input_file(file_in: str) -> list:
    '''
    Parses the input file into a list of coordinates
    Input Example:
        0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2
    '''
    with open(sys.argv[1], 'r') as input_fh:
        input_lines = input_fh.readlines()

    coords = [{
        'x1':int(x.split('->')[0].strip().split(',')[0]),
        'x2':int(x.split('->')[1].strip().split(',')[0]),
        'y1':int(x.split('->')[0].strip().split(',')[1]),
        'y2':int(x.split('->')[1].strip().split(',')[1]) 
        } for x in input_lines]
    return coords

def diag_line_to_coords(coords: dict) -> (list):
    '''
    Given a set of line endpoints, forming a diagonal line, returns a list of
    coordinates that are undeneath the line.
    '''
    coord_list = []

    print('='*80)
    print(coords)
    x1 = coords['x1']
    y1 = coords['y1']
    x2 = coords['x2']
    y2 = coords['y2']

    # Twin pairs line
    if x1 == y1 and x2 == y2:
        print('twin pairs line')
        x_start = min(x1, x2)
        x_end = max(x1, x2)
        y_start = min(y1, y2)
        y_end = max(y1, y2)
        print(x_start, x_end+1)
        print(y_start, y_end+1)
        x_coords = list(range(x_start, x_end+1))
        y_coords = list(range(y_start, y_end+1))
        coord_list = list(filter(lambda x: x[0] == x[1], list(zip(x_coords, y_coords))))
        pprint(coord_list)

#        # Mirror pairs - Not yet working
#        if coord['x1'] == coord['y2'] and coord['x2'] == coord['y1']:
#            print('MIRROR PAIRS')
#            print(coord)
#            x_range = range(int(coord['x1']), int(coord['x2']))
#            y_range = range(int(coord['y1']), int(coord['y2']))
#            print(list(x_range))
#            print(list(zip(x_range, y_range)))
##            for y, _ in enumerate(ht_map):
##                if y in range(coord['y1'], coord['y2']):
##                    for x, _ in enumerate(ht_map[0]):
##                        if x in range(min(coord['x1'], coord['x2'])):
##                            print(f'marking: {x}, {y}')
##                            ht_map[y][x] += 1
#                if x in range(min(coord['x1'], coord['x2']), max(coord['x1'], coord['x2'])):
#                    for y, _ in enumerate(ht_map):
#                        if y in range(min(coord['y1'], coord['y2']), max(coord['y1'], coord['y2'])):
#                            if x == y:
#                                #print(f'marking: {x}, {y}')
#                                ht_map[y][x] += 1
#    # Mirror pairs line
#    if x1 == y2 and x2 == y1:
#        print('mirror pairs line')
#        x_start = min(x1, x2)
#        x_end = max(x1, x2)
#        y_start = min(y1, y2)
#        y_end = max(y1, y2)
#        print(x_start, x_end+1)
#        print(y_start, y_end+1)
#        x_coords = list(range(x_start, x_end+1))
#        y_coords = list(range(y_start, y_end+1))
#        coord_list = list(filter(lambda x, y: x == y, list(zip(x_coords, y_coords))))
#        pprint(coord_list)
#        coord_list = []

    return coord_list

def hv_line_to_coords(coords: dict) -> (list):
    '''
    Given a set of line endpoints, forming a horizontal or vertical line, returns a list of
    coordinates that are undeneath the line.
    '''
    coord_list = []

    #print('='*80)
    #print(coord)
    x1 = coords['x1']
    y1 = coords['y1']
    x2 = coords['x2']
    y2 = coords['y2']

    # Vertical line
    if x1 == x2:
        #print('vertical line')
        start = min(y1, y2)
        end = max(y1, y2)
        #print(start, end+1)
        x_coords = [x1 for y in range(start, end+1)]
        y_coords = list(range(start, end+1))
        coord_list = list(zip(x_coords, y_coords))
        #pprint(coord_list)

    # Horizontal line
    if y1 == y2:
        #print('horizontal line')
        start = min(x1, x2)
        end = max(x1, x2)
        #print(start, end+1)
        x_coords = list(range(start, end+1))
        y_coords = [y1 for x in range(start, end+1)]
        coord_list = list(zip(x_coords, y_coords))
        #pprint(coord_list)

    return coord_list


def coords_to_map(lines: list) -> (list, int):
    '''
    Given a list of coords, draw a map of lines with the signifier
    being the number of lines overlapping at a given location.
    As a bonus, also returns the number of overlapping points.
    '''
    # First generate a base map with only zeros
    width = 10
    height = 10

    ht_map = []
    for x in range(width):
        ht_map.append([])
        ht_map[x] = []
        for y in range(height):
            ht_map[x].append(0)

    # Now fill the map in through each set of coords
    for line in lines:
        for coords in line:
            for (x, y) in coords:
                ht_map[y][x] += 1


    # Finally, swap 0's for '.'s and count the overlap
    overlap = 0
    for row_idx, row in enumerate(ht_map):
        overlap += len(list(filter(lambda x: x > 1, row)))
        ht_map[row_idx] = [str(col) if col > 0 else '.' for col in row]

    return ht_map, overlap

if __name__ == '__main__':
    ##########
    # Part 1 #
    ##########
    print('#'*25)
    print('Part 1: Hydrothermal slalom')
    print('#'*25)
    full_coords = []
    coords = parse_input_file(sys.argv[1])
    hv_line_coords = list(filter(lambda x: x['x1'] == x['x2'] or x['y1'] == x['y2'], coords))
    full_coords.append(list(map(hv_line_to_coords, hv_line_coords)))
    ht_map, overlap = coords_to_map(full_coords)
    print('Hydrothermal Map:')
    for row in ht_map:
        print(''.join(row))
    print(f'\nOverlapping points: {overlap}')

    ##########
    # Part 2 #
    ##########
    print('#'*25)
    print("Part 2: I guess we're just doing anything now")
    print('#'*25)

    full_coords = []
    coords = parse_input_file(sys.argv[1])
    diag_line_coords = list(filter(lambda x: (x['x1'] == x['y1'] and x['x2'] == x['y2']) or (x['x1'] == x['y2'] and x['x2'] == x['y1']), coords))
    hv_line_coords = list(filter(lambda x: x['x1'] == x['x2'] or x['y1'] == x['y2'], coords))
    full_coords.append(list(map(hv_line_to_coords, hv_line_coords)))
    full_coords.append(list(map(diag_line_to_coords, diag_line_coords)))
    ht_map, overlap = coords_to_map(full_coords)
    print('Hydrothermal Map:')
    for row in ht_map:
        print(''.join(row))
    print(f'\nOverlapping points: {overlap}')
