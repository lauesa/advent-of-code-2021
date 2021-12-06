import numpy as np
import collections


reading = 0
counter = 0
q = collections.deque(maxlen=3)
with open("input.txt") as file:
    for line in file:
        q.appendleft(int(line))
    
        r = sum(q)

        if reading and r > reading:
            counter +=1

        if len(q) == 3:
            reading = r
    
print(counter)