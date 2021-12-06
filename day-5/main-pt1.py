import numpy as np
from matplotlib import pyplot as plt

maxbreadth = 1000

cmap = np.zeros((maxbreadth,maxbreadth))
with open("input.txt") as file:
    for line in file:
        cmd = line.strip().split(' -> ')

        pt1 = cmd[0].split(',')
        pt2 = cmd[1].split(',')
        print '{} => {}'.format(pt1, pt2)
        # determine axis of change
        if int(pt1[0]) == int(pt2[0]):
            s = np.sign(int(pt2[1]) - int(pt1[1]))
            for y in range(int(pt1[1]), int(pt2[1]) + s, s * 1):
                cmap[int(pt1[0])][y] +=1
        elif int(pt1[1]) == int(pt2[1]):
            s = np.sign(int(pt2[0]) - int(pt1[0]))
            for x in range(int(pt1[0]), int(pt2[0]) + s, s * 1):
                cmap[x][int(pt1[1])] +=1

up = np.ix_(cmap.flatten()>1)
im = plt.imshow(cmap)
plt.show()
print np.count_nonzero(up)