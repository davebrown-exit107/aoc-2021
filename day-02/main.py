import os
import sys

location = {
        'depth': 0,
        'horiz': 0,
        'aim': 0,
        }

with open(sys.argv[1], 'r') as input_fh:
    directions = input_fh.readlines()
directions = [{'direction':x.strip().split(' ')[0], 'amount': int(x.strip().split(' ')[1])} for x in directions]
for direction in directions:
    if direction['direction'] == 'forward':
        location['horiz'] += direction['amount']
        location['depth'] += location['aim']*direction['amount']
    if direction['direction'] == 'down':
        location['aim'] += direction['amount']
    if direction['direction'] == 'up':
        location['aim'] -= direction['amount']

print(f"Overall depth: {location['depth']}")
print(f"Overall horiz: {location['horiz']}")
print(location['horiz']*location['depth'])
