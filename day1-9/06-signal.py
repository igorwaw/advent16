#!/usr/bin/python3

from collections import Counter

INPUTFILE="06-input.txt"

inputcols=[]

with open(INPUTFILE) as f:
    for line in f:
        for i,letter in enumerate( line.strip() ): # iterate over letters + get column number
            try:
                inputcols[i]+=letter
            except IndexError: # we don't have a string for this column yet (we're on line 1 of file)
                inputcols.append(letter)


message1=""
message2=""


for colnum,col in enumerate(inputcols):
    lettercount=Counter(col).most_common()
    # counter counts letters, most_common()  returns list of tuples 
    # with most common elements, first of tuple=most common letter, second=count of this letter
    # [0] to extract first pair of the dict (most common) or [-1] to extract least common
    # then [0] to extract first element of the tuple
    letter1=lettercount[0][0]
    letter2=lettercount[-1][0]
    #print(f"column {colnum}: {col}, most common {letter1} least common {letter2}")
    message1+=letter1
    message2+=letter2

print("Part 1, message: ", message1)
print("Part 2, message: ", message2)
