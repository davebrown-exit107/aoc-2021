import os
import sys

window = 3
overall = 0
inc = 0
dec = 0
nop = 0
with open(sys.argv[1], 'r') as input_fh:
    measurements = input_fh.readlines()

measurements = [int(x.strip()) for x in measurements]
for idx in range(len(measurements)):
    cur = sum(measurements[idx:idx + window])
    if idx == 0:
        prev = cur
    if cur > prev:
        delta = 'increased'
        inc +=1
        overall += 1
    if cur < prev:
        delta = 'decreased'
        dec += 1
        overall -= 1
    if cur == prev:
        delta = 'no change'
        nop += 1
    print(f'{cur} ({delta}:{overall})')
    prev = cur

print(f'Overall inc: {inc}')
print(f'Overall dec: {dec}')
print(f'Overall nop: {nop}')
print(f'Overall change: {overall}')
