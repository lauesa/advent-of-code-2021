a = 10
b = 5

import numpy as np

c = np.sign(b-a)
print c

for y in range(a, b + c, c * 1):
    print y