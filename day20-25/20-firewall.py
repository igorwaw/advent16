#!/usr/bin/python3


INPUTFILE="20-input.txt"
MAXIP=2**32

with open(INPUTFILE) as f:
    data=sorted(f.read().splitlines())
    ipranges=[ ( int(x),int(y) ) for x,y in [line.split("-")  for line in data ] ]

ipranges.sort()
num_valid=0
ip=0
part1done=False

for limit_l,limit_h in ipranges:
    if ip<limit_l: # outside the lower limit, valid IP
        num_valid+=limit_l-ip
        if not part1done:
            print(f"Part 1: {ip}")
            part1done=True
    ip=max(ip, limit_h+1) # skip past the end of the current blocklist
# add IPs from the end of the last blocklist till the max value
num_valid+=MAXIP-ip

print(f"Part 2: {num_valid}")
