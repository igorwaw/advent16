#!/usr/bin/python3

from collections import deque
import re
from dataclasses import dataclass
from itertools import chain, combinations
from copy import deepcopy


INPUTFILE="11-input.txt"

rx1=re.compile(r"(\w+) generator")
rx2=re.compile(r"(\w+)-compatible")




def is_valid_floor(floor: set) -> bool:
    # floor is valid if there's no generator...
    if not [e for e in floor if e[1]=="g" ]:
        return True
    # ...or for every chip there's a relevant generator
    return all( (e, "g") in floor for (e, device) in floor if device=="c" )

@dataclass
class Gamestate:
    elevator: int
    floors: list
    moves: int = 0

 
    def is_done(self) -> bool:
        global max_floor
        for i in range(max_floor-1):
            if len(self.floors[i]):
                return False
        return True

    def get_seen_state(self) -> str:
        retval=f"elevator:{self.elevator} "
        for i,floor in enumerate(self.floors):
            count_chips = sum(1 for _ in filter(lambda x: x[1]=="c", floor))
            count_rtgs = sum(1 for _ in filter(lambda x: x[1]=="g", floor))
            retval+=f"floor{i}:m{count_chips}g{count_rtgs} "
        return retval

    def print(self) -> None:
        global max_floor
        print(f"--- elevator: {self.elevator+1}   moves: {self.moves}  -----")
        for i in range(max_floor):
            print(f"Floor {i+1}: {self.floors[i]}  is valid? {is_valid_floor(self.floors[i])}")


def get_possible_moves(state: Gamestate) -> Gamestate:
    global max_floor
    current_floor=state.elevator
    devices_to_move=chain( combinations(state.floors[current_floor], 2), combinations(state.floors[current_floor], 1)  )
    for devs in devices_to_move:
        for i in [-1, 1]:
            next_floor=current_floor+i
            if next_floor<0 or next_floor>=max_floor:
                continue

            newstate=deepcopy(state)
            newstate.elevator=next_floor
            newstate.moves+=1
            newstate.floors[current_floor]=newstate.floors[current_floor].difference(devs)
            newstate.floors[next_floor]=newstate.floors[next_floor].union(devs)

            if (is_valid_floor(newstate.floors[current_floor]) and is_valid_floor(newstate.floors[next_floor])):
                yield newstate


def count_moves(state: Gamestate) -> int:
    seen = set()
    queue = deque([state])

    while queue:
        state = queue.popleft()
        if state.is_done():
            return state.moves
        
        for next_state in get_possible_moves(state):
            if (key := next_state.get_seen_state()) not in seen:
                seen.add(key)
                # next_state.print()
                queue.append(next_state)




# parse input
floors=[]
with open(INPUTFILE) as f:
    for i,line in enumerate(f):
        floors.append(set())
        for rtg in rx1.findall(line):
            floors[i].add( (rtg, "g") )
        for chip in rx2.findall(line):
            floors[i].add( (chip, "c") )

current_floor=0
max_floor=i+1

gamestate=Gamestate(current_floor, floors)
#gamestate.print()
print("Part 1: ") #47
print(count_moves(gamestate))
print("Part 2: ") #71
# reset and add devices
current_floor=0
floors[0]=floors[0].union([('elerium', 'g'), ('elerium', 'c'), ('dilithium', 'g'), ('dilithium', 'c')])
gamestate=Gamestate(current_floor, floors)
print(count_moves(gamestate))
