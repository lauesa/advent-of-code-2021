# map alpha inputs to a binary representation and match with a basic multiplexer

from collections import Counter

def seven_segment(number):
    # treat the number as a string, since that makes it easier to deal with
    # on a digit-by-digit basis
    digits = [representations[digit] for digit in str(number)]
    # now digits is a list of 5-tuples, each representing a digit in the given number
    # We'll print the first lines of each digit, the second lines of each digit, etc.
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))

# seven_segment(ord('a') - 97)

# 1 = 2
# 4 = 4
# 7 = 3
# 8 = 7

def decoder(code, input):
    disp = Counter(dict.fromkeys(range(-1, 9), 0))
    for act in input:
        if len(act) == 2:
            print('{} is 1'.format(act))
            disp[1] +=1
        elif len(act) == 4:
            # print('{} is 4'.format(act))
            disp[4] +=1
        elif len(act) == 3:
            # print('{} is 7'.format(act))
            disp[7] +=1
        elif len(act) == 7:
            # print('{} is 8'.format(act))
            disp[8] +=1
    
    return disp

disp = Counter(dict.fromkeys(range(-1, 9), 0))
with open("input.txt") as file:
    for i, line in enumerate(file):
        first, last = line.strip().split('|')
        first = first.strip().split(' ')
        last = last.strip().split(' ')
        disp += decoder(first, last)

print(sum(disp.values()))
        