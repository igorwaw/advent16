#!/usr/bin/python3

INPUT="00111101111101000"

def dragon(a: str) ->str:
    b="".join("0" if c=="1" else "1" for c in reversed(a))
    return a+"0"+b

def checksum(data: str) -> str:
    csum=""
    for i in range(0,len(data)-1,2):
        csum += "1" if data[i]==data[i+1] else "0"
    return csum if len(csum)%2 else checksum(csum)

def get_checksum_for_disk(initval: str, size: int):
    data=initval
    while len(data)<=size:
        data=dragon(data)
    data=data[:size]
    return checksum(data)

print(f"Part 1: {get_checksum_for_disk(INPUT,272)}")
print(f"Part 2: {get_checksum_for_disk(INPUT,35651584)}")
