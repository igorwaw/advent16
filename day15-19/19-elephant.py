#!/usr/bin/python3

from math import log

NUM_ELVES=3001330


def josephus(n: int) -> int:
    l = n - (1 << (n.bit_length() - 1))
    return 2*l + 1

def josephus2(n: int) -> int:
    if n<3:
        return 1
    exponent=int(log(n-1,3))
    closestpower=3**exponent
    if n-closestpower <= closestpower:
        return n-closestpower
    return 2*n-3*closestpower


print(f"Part 1, {josephus(NUM_ELVES)}")
print(f"Part 2, {josephus2(NUM_ELVES)}")
