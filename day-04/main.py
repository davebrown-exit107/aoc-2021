import os
import sys

from pprint import pprint

with open(sys.argv[1], 'r') as input_fh:
    input_lines = input_fh.readlines()

call_sequence = input_lines[0].split(',')
boards = []
cur_board = []
for line in input_lines[2:]:
    if line == '\n':
        boards.append(cur_board)
        cur_board = []
        continue
    cur_board.append(line.strip().split())

pprint(boards)

##########
# Part 1 #
##########
print('#'*25)
print('Part 1')
print('#'*25)

##########
# Part 2 #
##########
print('#'*25)
print('Part 2')
print('#'*25)
