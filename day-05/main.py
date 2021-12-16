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

def coords_to_map(coords: list) -> (list, int):
    '''
    Given a list of coords, draw a map of lines with the signifier
    being the number of lines overlapping at a given location.
    As a bonus, also returns the number of overlapping points.
    '''
    # First generate a base map with only zeros
    width = max([max([x['x1'] for x in coords]), max([x['x2'] for x in coords])])
    height = max([max([x['y1'] for x in coords]), max([x['y2'] for x in coords])])
    ht_map = []
    for x in range(width+1):
        ht_map.append([])
        ht_map[x] = []
        for y in range(height+1):
            ht_map[x].append(0)

    # Group the coordinates by the type of line
    diag_line_coords = list(filter(lambda x: (x['x1'] == x['y1'] and x['x2'] == x['y2']) or (x['x1'] == x['y2'] and x['x2'] == x['y1']), coords))
    hv_line_coords = list(filter(lambda x: x['x1'] == x['x2'] or x['y1'] == x['y2'], coords))

    # Now fill the map in through each set of coords
    # Horizontal/Vertical
    for coord in hv_line_coords:
        for x, _ in enumerate(ht_map[0]):
            # Horizontal lines
            if coord['x1'] == x and coord['x2'] == x:
                for y, _ in enumerate(ht_map):
                    if max(coord['y1'], coord['y2']) >= y >= min(coord['y1'], coord['y2']):
                        #print(f'marking: {x}, {y}')
                        ht_map[y][x] += 1

        for y, _ in enumerate(ht_map):
            # Vertical lines
            if coord['y1'] == y and coord['y2'] == y:
                for x, _ in enumerate(ht_map[0]):
                    if max(coord['x1'], coord['x2']) >= x >= min(coord['x1'], coord['x2']):
                        #print(f'marking: {x}, {y}')
                        ht_map[y][x] += 1

    # Diagonal
    for coord in diag_line_coords:
        # Twin pairs
        if coord['x1'] == coord['y1'] and coord['x2'] == coord['y2']:
            for x, _ in enumerate(ht_map[0]):
                if x in range(min(coord['x1'], coord['x2']), max(coord['x1'], coord['x2'])):
                    for y, _ in enumerate(ht_map):
                        if y in range(min(coord['y1'], coord['y2']), max(coord['y1'], coord['y2'])):
                            if x == y:
                                #print(f'marking: {x}, {y}')
                                ht_map[y][x] += 1

        # Mirror pairs - Not yet working
        if coord['x1'] == coord['y2'] and coord['x2'] == coord['y1']:
            for y, _ in enumerate(ht_map):
                if y in range(coord['y1'], coord['y2']):
                    for x, _ in enumerate(ht_map[0]):
                        if x in range(min(coord['x1'], coord['x2'])):
                            print(f'marking: {x}, {y}')
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

    coords = parse_input_file(sys.argv[1])
    hv_line_coords = list(filter(lambda x: x['x1'] == x['x2'] or x['y1'] == x['y2'], coords))
    ht_map, overlap = coords_to_map(hv_line_coords)
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

    coords = parse_input_file(sys.argv[1])
    diag_line_coords = list(filter(lambda x: (x['x1'] == x['y1'] and x['x2'] == x['y2']) or (x['x1'] == x['y2'] and x['x2'] == x['y1']), coords))
    hv_line_coords = list(filter(lambda x: x['x1'] == x['x2'] or x['y1'] == x['y2'], coords))
    print(diag_line_coords)
    mappable_lines = []
    mappable_lines.extend(diag_line_coords)
    mappable_lines.extend(hv_line_coords)
    ht_map, overlap = coords_to_map(mappable_lines)
    print('Hydrothermal Map:')
    for row in ht_map:
        print(''.join(row))
    print(f'\nOverlapping points: {overlap}')
