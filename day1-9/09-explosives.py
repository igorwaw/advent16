#!/usr/bin/python3

import re

INPUTFILE="09-input.txt"

rx1=re.compile( r"\((\d+)x(\d+)\)" )
 

def get_uncompressed_length(string: str, debug: bool=False, part2: bool=False) -> int:
    retval=0
    while string:
        marker=rx1.search(string)
        if not marker:
            retval+=len(string)
            break
        else:
            # we got the marker
            retval+=marker.start()
            length=int(marker.group(1))
            repeat=int(marker.group(2))
            if (debug):
                print(f"Checking {string}")
                print(f"    found marker: repeat {length} characters {repeat} times")
            if (part2):
                data_begin=marker.end()
                data_end=data_begin+length
                newdata=string[data_begin:data_end]*repeat
                retval+=get_uncompressed_length(newdata, debug=debug, part2=True)
            else:
                retval+=length*repeat
            newposition=marker.end()+length
            string=string[newposition:]
            if (debug):
                print(f"    searching new string {string}")
    return retval

with open(INPUTFILE) as f:
    part1length=0
    part2length=0
    for line in f:
        line="".join(line.split())
        part1length+=get_uncompressed_length(line, part2=False)
        part2length+=get_uncompressed_length(line, part2=True)

    print(f"Part 1: {part1length}")
    print(f"Part 2: {part2length}")