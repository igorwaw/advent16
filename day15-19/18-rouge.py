#!/usr/bin/python3


STARTROW="^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^"
NUMROWS1=40
NUMROWS2=400000


def get_next_row(oldrow: list) -> list:
    newrow=[]
    for i in range(len(oldrow)):
        left=oldrow[i-1] if i>=1 else 1
        right=oldrow[i+1] if i<len(oldrow)-1 else 1
        newrow.append(1 if left==right else 0)
    return newrow


row=[ 1 if x=="." else 0 for x in STARTROW ]
sumsafe=sum(row)
for i in range(NUMROWS2-1):
    row=get_next_row(row)
    sumsafe+=sum(row)
    if i==NUMROWS1-2:
        print(f"Part 1: {sumsafe}")        

print(f"Part 2: {sumsafe}")