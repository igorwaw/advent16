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

# print grid
width=max( node.x for node in grid )
height=max( node.y for node in grid )

gridmap=[[0 for _ in range(width+1)] for _ in range(height+1)]
for node in grid:
    gridmap[node.y][node.x]="█" if node.used>90 else "."
    if node.used==0:
        gridmap[node.y][node.x]="#"
        emptyx,emptyy=node.x, node.y
# show start and end node
gridmap[0][width]="S"
gridmap[0][0]="E"

wallbegin=min(node.x for node in grid if node.used>90)
wallsize=width+1-wallbegin

for row in gridmap:
    for d in row:
        print(d,end="")
    print("")

print(f"Width {width} height {height} empty node {emptyx, emptyy} wall size {wallsize}")

part2=(emptyx+1-wallbegin)+emptyy+wallsize+(width-1)*5
print(f"Part 2: {part2}")