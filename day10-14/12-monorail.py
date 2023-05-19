#!/usr/bin/python3


INPUTFILE="12-input.txt"

class Computer:
    register: dict = {}
    pointer: int = 0
    instructions: list[str]

    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self.instructions = f.read().splitlines()
        self.reset()

    def reset(self) -> None:
        self.register["a"]=0
        self.register["b"]=0
        self.register["c"]=0
        self.register["d"]=0
        self.pointer=0


    def __repr__(self) -> str:
        return f"Registers: {self.register} pointer {self.pointer} current instruction {self.instructions[self.pointer]}"

    def get(self, arg: str) -> int:
        try:
            return int(arg)
        except ValueError:
            return self.register[arg]

    def run(self, debug=False) -> None:
        while self.pointer<len(self.instructions):
            cmd=self.instructions[self.pointer].split()
            if (debug): print(self)
            self.pointer+=1  # will have to decrease by 1 for jumps
            match cmd:
                case ("cpy", arg, target):
                    self.register[target]=self.get(arg)
                case ("inc", arg):
                    self.register[arg]+=1
                case ("dec", arg):
                    self.register[arg]-=1
                case ("jnz", testval, offset):
                    self.pointer += int(offset) -1 if self.get(testval)!=0 else 0
                case _: raise ValueError
        


computer=Computer("12-input.txt")
computer.run(debug=False)
print("Part 1, register A: ",computer.register["a"])
computer.reset()
computer.register["c"]=1
computer.run(debug=False)
print("Part 2, register A: ",computer.register["a"])