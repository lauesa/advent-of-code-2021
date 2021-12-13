# Python + Z3

from functools import reduce
from itertools import combinations
from z3 import *

vals = dict(zip('abcdefg', range(1, 8)))
inv_vals = dict((v, k) for k, v in vals.items())
# must be sorted to match
maps = ["cagedb", "ab", "gcdfa", "fbcad", "abef",
        "cdfbe", "cdfgeb", "dab", "acedgfb", "cefabd"]

digits = []
for digit in maps:
    s = sorted(digit)
    digits.append("".join(s))

of_length = reduce(lambda h, k: h.setdefault(
    len(k), []).append(k) or h, digits, {})

# this builds a list of linear statements [b + f + a == 10] [a + f + d + g == 15] [a + f == 9]

def add_clause(k, vars):
    # print(vars)
    ors = []
    summand = reduce(lambda a, b: a + b, [vars[c] for c in k])

    # generates bool ors of each length. converts the individual numbers into a parsable format for the sat solver with [b + f + a == 10] being the expression
    for k_ in of_length[len(k)]:
        # print(k_)
        # print([vals[c] for c in k_])
        # print(sum(vals[c] for c in k_))
        # print(summand == sum(vals[c] for c in k_))
        ors.append(summand == sum(vals[c] for c in k_))
    # print(ors)
    return Or(ors)


def parse(m, vars, k):
    # generates the output using the solver model for each letter of the graph

    # print([inv_vals[m[vars[c]].as_long()] for c in k])
    segs = sorted([inv_vals[m[vars[c]].as_long()] for c in k])
    # print(segs)

    return digits.index(''.join(segs))


def solve_line(l):
    inp, outp = l.split(" | ")
    s = Solver()
    a, b, c, d, e, f, g = Ints('a b c d e f g')
    vars = dict(zip('abcdefg', [a, b, c, d, e, f, g]))

    # creates a mapping across the various combinations making sure none of the combinations are equal
    for n, (i1, i2) in enumerate(combinations([a, b, c, d, e, f, g], 2)):
        # print('{}, {}'.format(i1, i2))

        s.add(i1 != i2)

    # builds boolean mappings for each unique set of wires [b + f + a == 10]
    for observed in inp.split():
        s.add(add_clause(observed, vars))
    s.check()
    m = s.model()
    return [parse(m, vars, k) for k in outp.split()]

# out = 0
# with open("input.txt") as file:
#     for i, line in enumerate(file):
#         out +=(int("".join(map(str, (solve_line(line))))))
# print(out)

# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, 0]

# using reduce to compute sum of list
print("The sum of the list elements is: {}".format(functools.reduce(lambda a, b: a+b, lis)))

# using reduce to compute maximum element from list
print("The maximum element of the list is: {}".format(functools.reduce(lambda a, b: a if a > b else b, lis)))