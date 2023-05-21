#!/usr/bin/python3

import hashlib
import re
from functools import cache

SALT="ahsbgdzn"
has3=re.compile(r"(\w)\1\1")

@cache
def gethash(i: int) -> str:
    newid=SALT+str(i)
    return hashlib.md5(newid.encode()).hexdigest()
# execution time: 2.6 vs 0.5

@cache
def getstretchedhash(i: int) -> str:
    newid=SALT+str(i)
    stretchedhash= hashlib.md5(newid.encode()).hexdigest()
    for _ in range(2016):
        stretchedhash=hashlib.md5(stretchedhash.encode()).hexdigest()
    return stretchedhash

def check5(startindex: int, text: str, stretched=False) -> int:
    for i in range(startindex+1,startindex+1000):
        nexthash = getstretchedhash(i) if stretched else gethash(i)
        if text in nexthash:
            return i
    return 0

# part1

def get64hashes(stretched=False, debug=False) -> int:
    i=0
    num_hashes=0
    while True:
        nexthash=getstretchedhash(i) if stretched else gethash(i)
        if m:=has3.search((nexthash)):
            matched=m.group(1)
            if index_of_5:=check5(i,matched*5, stretched):
                num_hashes+=1
                if (debug):
                    print(f"Got new hash number {num_hashes} at index {i}")
                if num_hashes==64:
                    return i
        i+=1

print(f"Part 1: {get64hashes(stretched=False)}")
print(f"Part 2: {get64hashes(stretched=True)}")

