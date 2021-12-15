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
boards.append(cur_board)

pprint(boards)

##########
# Part 1 #
##########
print('#'*25)
print('Part 1: Fighting the squid')
print('#'*25)

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


def play_bingo(boards: list, call_sequence: list) -> (int, int):
    '''
    Walk through the call_sequence and mark boards, if a bingo is
    found, return the board index and current step.
    '''
    for step, num in enumerate(call_sequence):
        for w, board in enumerate(boards):
            for x, row in enumerate(board):
                for y, col in enumerate(row):
                    if col == num:
                        boards[w][x][y] = 'X'
                        if check_board(boards[w]):
                            return w, step
        print('#'*50)
        print(f'{step} ({num})')
        print('#'*50)
        #pprint(boards)
        print('#'*50)


winning_board_idx, winning_step = play_bingo(boards, call_sequence)
print(f'board {winning_board_idx} wins on step {winning_step} ({call_sequence[winning_step]})')
pprint(boards[winning_board_idx])
score = calculate_score(boards[winning_board_idx], winning_step)
print(f'winning board score: {score}')

##########
# Part 2 #
##########
print('#'*25)
print('Part 2: Admitting defeat')
print('#'*25)

def lose_bingo(boards: list, call_sequence: list) -> (list, int):
    '''
    Walk through the call_sequence and mark boards, if a bingo is
    found check to see if it is the last board to have a bingo,
    then return the board and the step in the call sequence.
    '''
    for step, num in enumerate(call_sequence):
        for w, board in enumerate(boards):
            for x, row in enumerate(board):
                for y, col in enumerate(row):
                    if col == num:
                        boards[w][x][y] = 'X'
                        if check_board(boards[w]):
                            winner = boards.pop(w)
                            if len(boards) == 0:
                                return winner, step
        print('#'*50)
        print(f'{step} ({num})')
        print('#'*50)
        #pprint(boards)
        print('#'*50)


winning_board, winning_step = lose_bingo(boards, call_sequence)
print(f'last winning board wins on step {winning_step} ({call_sequence[winning_step]})')
pprint(winning_board)
score = calculate_score(winning_board, winning_step)
print(f'winning board score: {score}')

