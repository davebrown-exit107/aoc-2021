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

def check_board(board: list) -> bool:
    '''
    Check the board to see if there are any bingos.
    '''
    # Check horizontal
    for row in board:
        if row == ['X', 'X', 'X', 'X', 'X']:
            return True

    # Check vertical
    for idx in range(len(board[0])):
        if len([x[idx] for x in board if x[idx] == 'X']) == 5:
            return True

def calculate_score(board: list, step: int) -> int:
    '''
    Calculate the score of a marked board.
    '''
    total = 0
    for row in board:
        for col in row:
            if col != 'X':
                total += int(col)

    return total * int(call_sequence[step])

def mark_boards(boards: list, val: str) -> list:
    '''
    Mark the boards in the provided list with an 'X' when the value matches.
    '''
    for board_idx, board in enumerate(boards):
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                if col == val:
                    boards[board_idx][row_idx][col_idx] = 'X'
    return boards

def play_bingo(boards: list, call_sequence: list) -> (list, int):
    '''
    Walk through the call_sequence and mark boards, if a bingo is
    found, return the board index and current step.
    '''
    for step, num in enumerate(call_sequence):
        boards = mark_boards(boards, num)
        winner = list(filter(check_board, boards))
        if len(winner) > 0:
            return winner[0], step

def lose_bingo(boards: list, call_sequence: list) -> (list, int):
    '''
    Walk through the call_sequence and mark boards, if a bingo is
    found check to see if it is the last board to have a bingo,
    then return the board and the step in the call sequence.
    '''
    winning_sequence = []
    for step, num in enumerate(call_sequence):
        boards = mark_boards(boards, num)
        boards = list(filter(lambda x: not check_board(x), boards))
        #print(len(winner), len(boards))
        if len(boards) == 1:
            return boards, step

if __name__ == '__main__':
    ##########
    # Part 1 #
    ##########
    print('#'*25)
    print('Part 1: Hydrothermal slalom')
    print('#'*25)

    coords = parse_input_file(sys.argv[1])
    pprint(coords)

    ##########
    # Part 2 #
    ##########
    print('#'*25)
    print('Part 2: Admitting defeat')
    print('#'*25)
