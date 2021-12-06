

get_bin = lambda x, n: format(x, 'b').zfill(n)


# generate gamma and e rate then multiple to find power consumption
import numpy as np
import copy
from bitstring import BitArray
binsize = 12
stack = []
lc = 0
with open("input.txt") as file:
    for line in file:
        lc+=1
        stack.append([int(d) for d in '{}'.format(get_bin(int(line, 2), binsize))])

lstack = copy.deepcopy(stack)
stack = np.array(stack)
for idx in range(binsize):
    active = [item[idx] for item in stack]
    counts = np.bincount(active)
    try:
        if counts[0] == counts[1]:
            flag = 1
        else:
            flag = np.argmax(counts)
    except Exception as e:
        flag = np.argmax(counts)
    stack = [row for row in stack if row[idx]==flag]
    if len(stack) == 1:
        break

ogr = BitArray(stack[0]).uint

for idx in range(binsize):
    active = [item[idx] for item in lstack]
    counts = np.bincount(active)
    if counts[0] == counts[1]:
        flag = 0
    else:
        flag = np.argmin(counts)
    lstack = [row for row in lstack if row[idx]==flag]
    if len(lstack) == 1:
        break

co2 = BitArray(lstack[0]).uint
print co2 * ogr
