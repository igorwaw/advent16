#!/usr/bin/python3

import hashlib
from dataclasses import dataclass
from typing import Tuple
from collections import deque

PASSCODE="pslxynzg"
WIDTH=4
HEIGHT=4
DIRECTIONS=( (0,-1), (0,1), (-1,0), (1,0) ) 
DIRNAME={ (0,-1):"U", (0,1):"D", (-1,0):"L", (1,0):"R" }


def gethash(i: str) -> str:
    return hashlib.md5(i.encode()).hexdigest()[:4]

def door_open(char: str) -> bool:
    return char in "bcdef"

@dataclass(frozen=True)
class Gamestate:
    x: int = 1
    y: int = 1
    path: str=""

    def get_next_dir(self) -> Tuple[int, int]:
        doorhash=gethash(PASSCODE+self.path)
        for (door, direction) in zip(doorhash,DIRECTIONS):
            (deltax,deltay)=direction           
            if self.x+deltax<1 or self.x+deltax>WIDTH:
                continue
            if self.y+deltay<1 or self.y+deltay>HEIGHT:
                continue
            if door_open(door):
                yield direction


def get_path(start_point: Gamestate, end_point: Tuple[int, int]) -> str:
    to_check=deque()
    to_check.append(start_point)
    while to_check:
        current_point=to_check.popleft()
        for dir in current_point.get_next_dir():
            newpath=current_point.path+DIRNAME[dir]
            newx=current_point.x+dir[0]
            newy=current_point.y+dir[1]
            if newx==end_point[0] and newy==end_point[1]:
                return newpath
            newpoint=Gamestate(newx, newy, newpath)
            #print(f"newpoint: {newpoint}")
            to_check.append(newpoint)


start=Gamestate()
end=(4,4)
print(f"Part 1: { get_path(start,end)  }")
