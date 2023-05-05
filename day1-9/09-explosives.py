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
                print(f"found marker: repeat {length} characters {repeat} times")
            retval+=length*repeat
            newposition=marker.end()+length
            string=string[newposition:]
            if (debug):
                print(f"    searching new string {string}")
    return retval

with open(INPUTFILE) as f:
    totallength=0
    for line in f:
        line="".join(line.split())
        #print(line, end=" ")
        length=get_uncompressed_length(line, part2=False)
        print (f"Uncompressed line length: {length}")
        totallength+=length

    print(f"Part 1: {totallength}")

