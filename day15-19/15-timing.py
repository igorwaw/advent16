#!/usr/bin/python3

from functools import reduce

INPUTFILE="15-input.txt"

def chinese_remainder(divisors: list, residues: list) -> int:
    csum = 0
    prod = reduce(lambda acc, b: acc*b, divisors)
    for divisor_i, a_i in zip(divisors, residues):
        p = prod // divisor_i
        csum += a_i * modular_inverse(p, divisor_i) * p
    return csum % prod
 
 

def modular_inverse(a: int, b: int) -> int:
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def get_residues(positions: list, sizes: list) -> list:
    residues=[]
    for i, (position, size) in enumerate(zip(positions, sizes)):
        newposition=(size-position-i)%size
        residues.append(newposition)
    return residues

def brute_force(sizes: list, positions: list) -> int:
    t=0
    while True:
        if all( (t+startpos+num)%size==0 for num,(startpos,size) in enumerate(zip(positions,sizes)) ):
            return t
        t+=1

# parse input
sizes=[]
positions=[]
with open(INPUTFILE) as f:
    for line in f:
        splitline=line.rstrip().split()
        size=int(splitline[3])
        position=int(splitline[11][:-1]) # skip last character - dot
        sizes.append(size)
        positions.append(position)


residues=get_residues(positions, sizes)
print(f"Disc sizes: {sizes}")
print(f"Disc positions: {positions}")
print(f"Residues: {residues}")

part1crt=chinese_remainder(sizes, residues)-1
part1force=brute_force(sizes,positions)-1

print(f"Part 1, Chinese Remainder Theorem: {part1crt}")
print(f"Part 1, brute force: {part1force}")

#part 2
sizes.append(11)
positions.append(0)
residues=get_residues(positions, sizes)
part2crt=chinese_remainder(sizes, residues)-1
part2force=brute_force(sizes,positions)-1
print(f"Part 2, Chinese Remainder Theorem: {part2crt}")
print(f"Part 2, brute force: {part2force}")
