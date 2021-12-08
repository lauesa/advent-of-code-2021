import numpy as np
import math

def crab_dist1(input):
    pos = np.median(input)
    print 'align to {}'.format(pos)
    print sum(abs(input - np.full(input.shape, pos)).astype(int))

def crab_dist2(input):
    pos = math.floor(np.mean(input))
    print 'align to {}'.format(pos)
    fuel = 0
    dist = abs(input - np.full(input.shape, pos)).astype(int)
    for d in dist:
        for x in range(1, d+1):
            fuel += x
    print fuel

with open("input.txt") as file:
    for i, line in enumerate(file):
        if i == 0:
            data = np.asarray(line.strip().split(',')).astype(int)

crab_dist1(data)
crab_dist2(data)