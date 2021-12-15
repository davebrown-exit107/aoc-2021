import os
import sys

gamma = ['0','b']
epsilon = ['0','b']

with open(sys.argv[1], 'r') as input_fh:
    input_lines = input_fh.readlines()
input_formatted = [x.strip() for x in input_lines]

for idx in range(len(input_formatted[0])):
    one = len([x[idx] for x in input_formatted if x[idx] == '1'])
    zero = len([x[idx] for x in input_formatted if x[idx] == '0'])
    print(f'idx: {idx}')
    print(f'one: {one}')
    print(f'zero: {zero}')
    if one > zero:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')
gamma_dec = int(''.join(gamma), 2)
epsilon_dec = int(''.join(epsilon), 2)
print(f'gamma: {gamma_dec}\nepsilon: {epsilon_dec}\npower: {gamma_dec * epsilon_dec}')
