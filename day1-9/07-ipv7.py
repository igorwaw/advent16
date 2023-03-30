#!/usr/bin/python3

import re

INPUTFILE="07-input.txt"


rx1=re.compile(r"(\w)(\w)\2\1")  # check for reversed pair, eg. abba, but will also catch aaaa
rx2=re.compile(r"\[\w*(\w)(\w)\2\1\w*]") # check for reversed pair in square brackets
rx3=re.compile(r"(\w)\1{3}") # check for "reversed pair" of same characters



def check_tls(line):
    if m:=rx2.search(line):
            #print(f"Reversed pair in brackets: {m.group()}, no TLS in {line}")
            return False
    if m:=rx3.search(line):
            #print(f"'Reversed pair' of same characters: {m.group()}, no TLS in {line}")
            return False
    if m:=rx1.search(line):
            #print(f"Match found: {m.group()}  TLS in {line}")
            return True
    return False


def check_ssl(line):
    in_hyper_block=False
    hyper_matches=set()
    no_hyper_matches=set()
    for i in range(len(line)-2): # we're looking 2 characters ahead from current index
        if line[i]=="[":
            in_hyper_block=True
        elif line[i]=="]":
            in_hyper_block=False
        else:
             if line[i]==line[i+2] and line[i]!=line[i+1]:  # found aba block
                if in_hyper_block:
                    hyper_matches.add(line[i]+line[i+1])
                else:
                    no_hyper_matches.add(line[i+1]+line[i]) # reverse block
        if hyper_matches & no_hyper_matches:
            return True
    return False


tlscount=0
sslcount=0
with open(INPUTFILE) as f:
    for line in f:
        line=line.strip()
        if check_tls(line):
            tlscount+=1
        if check_ssl(line):
            sslcount+=1

print("Part 1, TLS addresses: ", tlscount)
print("Part 2, SSL addresses: ", sslcount)
