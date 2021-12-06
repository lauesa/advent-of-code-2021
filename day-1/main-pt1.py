import numpy as np


reading = 0
counter = 0
with open("input.txt") as file:
    for line in file:
        if int(line) > reading and reading != 0:
            counter +=1
        reading = int(line)

print(counter)