import os
import sys

gamma = ['0','b']
epsilon = ['0','b']

with open(sys.argv[1], 'r') as input_fh:
    input_lines = input_fh.readlines()
input_formatted = [x.strip() for x in input_lines]

##########
# Part 1 #
##########
print('#'*25)
print('Part 1')
print('#'*25)
for idx in range(len(input_formatted[0])):
    one = len([x[idx] for x in input_formatted if x[idx] == '1'])
    zero = len([x[idx] for x in input_formatted if x[idx] == '0'])
    #print(f'idx: {idx}')
    #print(f'one: {one}')
    #print(f'zero: {zero}')
    if one >= zero:
        oxy_gen_indicator = '1'
        c02_scrub_indicator = '0'
        gamma.append('1')
        epsilon.append('0')
    else:
        oxy_gen_indicator = '0'
        c02_scrub_indicator = '1'
        gamma.append('0')
        epsilon.append('1')
gamma_dec = int(''.join(gamma), 2)
epsilon_dec = int(''.join(epsilon), 2)
print(f'gamma: {gamma_dec}\nepsilon: {epsilon_dec}\npower: {gamma_dec * epsilon_dec}')

##########
# Part 2 #
##########
print('#'*25)
print('Part 2')
print('#'*25)
def filter_lcv(list_in, idx):
    if len(list_in) == 1:
        return int(list_in[0], 2)
    else:
        #print(f'{len(list_in)} not short enough')
        one = len([x[idx] for x in list_in if x[idx] == '1'])
        zero = len([x[idx] for x in list_in if x[idx] == '0'])
        if one >= zero:
            lcv = '0'
        elif zero > one:
            lcv = '1'

        #print(idx)
        #print([x[idx] for x in list_in])
        #print(list_in)
        return filter_lcv(list(filter(lambda x: x[idx] == lcv, list_in)), idx+1)

def filter_mcv(list_in, idx):
    if len(list_in) == 1:
        return int(list_in[0], 2)
    else:
        #print(f'{len(list_in)} not short enough')
        one = len([x[idx] for x in list_in if x[idx] == '1'])
        zero = len([x[idx] for x in list_in if x[idx] == '0'])
        if one >= zero:
            mcv = '1'
        elif zero > one:
            mcv = '0'

        #print(idx)
        #print([x[idx] for x in list_in])
        #print(list_in)
        return filter_mcv(list(filter(lambda x: x[idx] == mcv, list_in)), idx+1)

oxy_rating = filter_mcv(input_formatted, 0)
co2_rating = filter_lcv(input_formatted, 0)
life_support_rating = oxy_rating * co2_rating
print(f'Oxygen rating: {oxy_rating}\nCO2 scrubber rating: {co2_rating}\nLife Support Rating: {life_support_rating}')
