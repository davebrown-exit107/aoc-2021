import os
import sys

from pprint import pprint

def parse_input_file(file_in: str) -> (list, list):
    '''
    Parses the input file into a list of boards and the call sequence
    '''
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
    boards.append(cur_board)
    return boards, call_sequence

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
    print('Part 1: Fighting the squid')
    print('#'*25)
    boards, call_sequence = parse_input_file(sys.argv[1])
    winning_board, winning_step = play_bingo(boards, call_sequence)
    print(f'board wins on step {winning_step} ({call_sequence[winning_step]})')
    pprint(winning_board)
    score = calculate_score(winning_board, winning_step)
    print(f'winning board score: {score}')

    ##########
    # Part 2 #
    ##########
    print('#'*25)
    print('Part 2: Admitting defeat')
    print('#'*25)
    boards, call_sequence = parse_input_file(sys.argv[1])
    winning_board, winning_step = lose_bingo(boards, call_sequence)
    real_winning_board, real_winning_step = play_bingo(winning_board, call_sequence[winning_step:])
    print(f'last winning board wins on step {winning_step} ({call_sequence[winning_step]})')
    pprint(winning_board)
    score = calculate_score(real_winning_board, winning_step+real_winning_step)
    print(f'winning board score: {score}')
