#!/usr/bin/python3

import re
from dataclasses import dataclass

INPUTFILE="22-input.txt"

@dataclass(frozen=True)
class Node:
    x: int
    y: int
    size: int
    used: int
    available: int

rx1=re.compile(r"x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T")

grid=[]

with open(INPUTFILE) as f:
    for i, line in enumerate(f):
        if i<=1:
            continue
        m=rx1.search(line)
        grid.append(Node( *map(int,m.groups() )))

viable=0

print(grid[2])

for nodeA in grid:
    if nodeA.used==0:
        continue
    for nodeB in grid:
        if nodeA!=nodeB and nodeA.used<=nodeB.available:
            viable+=1

print(f"Part 1: {viable}")
