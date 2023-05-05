#!/usr/bin/python3

from dataclasses import dataclass

INPUTFILE="01-input.txt"


#immutable data class
@dataclass(frozen=True)
class Point:
    x: int
    y: int

# read input file
with open(INPUTFILE) as f:
    line=f.readline().strip()
    directions=line.split(", ")


current=Point(0,0)
visited=set()
visited.add(current)
direction=0 # 0=N, 1=E, 2=S, 3=W
part2done=False
for i in directions:
    move=int(i[1:])
    if i[0]=="R":
        direction=(direction+1)%4
    else:
        direction=(direction-1)%4
    #print(direction)
    newx=current.x
    newy=current.y
    for j in range(move):
        if direction==0:
            newy+=1
        elif direction==1:
            newx+=1
        elif direction==2:
            newy-=1
        elif direction==3:
            newx-=1
        current=Point(newx, newy)
        #print(current)
        if (not part2done) and (current in visited):
            print("Visited twice: ", current)
            #calculate distance
            print("Distance (part 2): ", abs(current.x)+abs(current.y))
            part2done=True
        # add current to visited
        visited.add(current)



# calculate distance
print("Final position: ", current)
print("Distance (part 1): ", abs(current.x)+abs(current.y))

