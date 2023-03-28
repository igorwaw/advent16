#!/usr/bin/python3

import re
from collections import Counter


rx1=re.compile(r"([a-z-]+)([0-9]+)\[([a-z]+)\]")


INPUTFILE="04-input.txt"

def calculate_sum(name):
    lettercounter=Counter(name).most_common()
    sortedcounter=sorted(lettercounter, key=lambda x: (-x[1],x[0]))
    checksum=""
    num=0
    for l,_ in sortedcounter[:5]:
        checksum+=l
    return checksum

#part 1
sum_sector=0
with open(INPUTFILE) as f:
    for line in f:
        roomsearch=rx1.search(line)
        if roomsearch:
            roomname, roomsector, roomsum=roomsearch.groups()
            roomname=roomname.replace("-","")
            newsum=calculate_sum(roomname)
            if roomsum == newsum:
                #print(f"Correct room: {roomname}, sector {roomsector}, checksum {roomsum}")
                sum_sector+=int(roomsector)
            else:
                #print(f"Fake room: {roomname}, sector {roomsector}, checksum read {roomsum}, calculated {newsum}")
                pass
        else:
            print("Wrong room format (or wrong regexp): ", line)
print("Part 1, sum of sectors: ", sum_sector)