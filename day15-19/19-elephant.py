#!/usr/bin/python3

from __future__ import annotations

NUM_ELVES=3001330

class Elf:
    number: int = 0
    left: Elf
    right: Elf
    id: int

    def __init__(self, r: Elf=None) -> None:
        self.left=None
        self.right=r
        Elf.number+=1
        self.id=Elf.number
    
    def remove(self, debug=False) -> None:
        self.left.right=self.right
        self.right.left=self.left
        Elf.number-=1
        if debug:
            print(f"Removing elf {self.id} elves left {Elf.number}")



def create_elves(first_elf: Elf) -> None:
    last_elf=first_elf
    for _ in range(NUM_ELVES-1):
        new_elf=Elf(r=last_elf)
        last_elf.left=new_elf
        last_elf=new_elf
    #make it circular
    last_elf.left=first_elf
    first_elf.right=last_elf

def remove_elves(part2=False) -> int:
    current_elf=first_elf
    while Elf.number>1:
        current_elf.left.remove()
        current_elf=current_elf.left
    return current_elf.id

### MAIN

print(f"Creating {NUM_ELVES} elves...")

first_elf=Elf()
create_elves(first_elf)

print(f"Done, number of elves: {Elf.number}")


print(f"Part 1, elf left: {remove_elves(part2=False)}")
