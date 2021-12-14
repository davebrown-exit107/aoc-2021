import os
import sys

overall = 0
inc = 0
dec = 0
nop = 0
with open(sys.argv[1], 'r') as input_fh:
    for idx, x in enumerate(input_fh.readlines()):
        if idx == 0:
            prev = x
        if x > prev:
            delta = 'increased'
            inc +=1
            overall += 1
        if x < prev:
            delta = 'decreased'
            dec += 1
            overall -= 1
        if x == prev:
            delta = 'no change'
            nop += 1
        print(f'{x} ({delta}:{overall})')
        prev = x

print(f'Overall inc: {inc}')
print(f'Overall dec: {dec}')
print(f'Overall nop: {nop}')
print(f'Overall change: {overall}')
