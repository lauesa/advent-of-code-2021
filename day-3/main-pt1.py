



# generate gamma and e rate then multiple to find power consumption
import numpy as np
binsize = 12
count = np.zeros((binsize,1))
lc = 0
with open("input.txt") as file:
    for line in file:
        lc+=1
        line = int(line, 2)
        for N in range(binsize):
            if line & (1 << N):
                count[N] +=1

rg = np.round(count/lc, 0)
gamma = 0
epsilon = 0
for M, b in enumerate(rg):
    if bool(b):
        gamma += (1 << M)
    else:
        epsilon += (1 << M)

print gamma * epsilon