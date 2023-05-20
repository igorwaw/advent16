#!/usr/bin/python3

from dataclasses import dataclass
from collections import deque
from os import get_terminal_size

FAVNUM=1350
#FAVNUM=10

MAXX=MAXY=200
MAXDISTANCE=9999

@dataclass(frozen=True)
class Point:
    x: int
    y: int

class Map:
    distance: dict={}

    def __init__(self):
        for x in range(MAXX):
            for y in range(MAXY):
                self.distance[Point(x, y)] = MAXDISTANCE
        self.distance[Point(1,1)]=0

    def print(self):
        width = min(get_terminal_size()[0]//3,MAXX)
        height = min(get_terminal_size()[1]-3,MAXX)
        for y in range(height):
            for x in range(width):
                p=Point(x,y)
                if is_empty(p):
                    d=self.distance[p]
                    if d<MAXDISTANCE:
                        print(f"{d:02d}", end=" ")
                    else:
                        print("   ", end="")
                else:
                    print("███", end="")
            print("")

            



def is_empty(point: Point) -> bool:
    v = point.x**2 + 3*point.x + 2*point.x*point.y + point.y + point.y**2 + FAVNUM
    return v.bit_count() %2==0


def get_next_points(p: Point) -> Point:
    global floormap
    for deltax in [-1, 0, 1]:
        for deltay in [-1, 0, 1]:
            if abs(deltax)==abs(deltay): # don't go diagonal
                continue
            newx=p.x+deltax
            newy=p.y+deltay
            if newx<0 or newy<0 or newx>=MAXX or newy>=MAXY:
                continue
            newpoint=Point(newx, newy)
            if not is_empty(newpoint):
                continue
            newdistance=floormap.distance[p]+1
            floormap.distance[newpoint]=min(floormap.distance[newpoint],newdistance)
            yield newpoint

def calculate_distances(target: Point) -> int:
    global floormap
    start_point=Point(1,1)
    visited=set()
    to_check=deque()
    to_check.append(start_point)
    visited.add(start_point)
    while to_check:
        current_point=to_check.popleft()
        for p in get_next_points(current_point):
            if p in visited:
                continue
            if p==target:
                return floormap.distance[p]
            to_check.append(p)
            visited.add(p)


floormap=Map()
part1answer=calculate_distances(Point(31,39))
print(f"Part 1: {part1answer}")
part2answer = sum(v <= 50 for v in floormap.distance.values())
print(f"Part 2: {part2answer}")
#floormap.print()