#!/usr/bin/python3

INPUTFILE="10-input.txt"

def parsebot(line: str) -> None:
    print(f"BOT: {line}")

def parsevalue(line: str) -> None:
    print(f"VALUE: {line}")


with open(INPUTFILE) as f:
    for line in f:
        if line.startswith("bot"):
            parsebot(line.strip())
        else:
            parsevalue(line.strip())