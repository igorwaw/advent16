#!/usr/bin/python3


INPUTFILE="23-input.txt"

class Computer:
    register: dict = {}
    pointer: int = 0
    instructions: list[str]

    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self.instructions = f.read().splitlines()
        self.reset()
        self.optimize()

    def reset(self) -> None:
        self.register["a"]=0
        self.register["b"]=0
        self.register["c"]=0
        self.register["d"]=0
        self.pointer=0

    def optimize(self) -> None:
        for i,instr in enumerate(self.instructions):
            cmd=instr.split()
            if cmd[0]=="jnz" and cmd[2]=="-5":
                jmpreg=cmd[1] # register to check for jnz
                cmd1=self.instructions[i-5].split() # inner loop
                cmd2=self.instructions[i-1].split() # counter for jump
                cmd3=self.instructions[i-4].split() # target register
                jmpreset=cmd1[2] # register reset

                targetreg1=cmd1[1]
                targetreg2=cmd2[1]
                targetval=cmd3[1]
                newcmd=f"mul {targetreg1} {targetreg2} {targetval}"
                self.instructions[i-5]=newcmd
                self.instructions[i-4]="nop"
                self.instructions[i-3]="nop"
                self.instructions[i-2]="nop"
                self.instructions[i-1]=f"cpy 0 {jmpreset}"  
                self.instructions[i]=f"cpy 0 {jmpreg}"  


    def __repr__(self) -> str:
        return f"Registers: {self.register} pointer {self.pointer} current instruction {self.instructions[self.pointer]}"

    def get(self, arg: str) -> int:
        try:
            return int(arg)
        except ValueError:
            return self.register[arg]

    def toggle(self, arg: str, debug=False) -> None:
        offset=self.get(arg)-1
        try:
            oldinstr=self.instructions[self.pointer+offset]
        except IndexError:
            if debug:
                print(f"Toggle: index {self.pointer+offset} out of range")
            return
        cmd=oldinstr.split()
        match cmd:
            case ("inc", arg):
                newinstr=f"dec {arg}"
            case (_, arg):
                newinstr=f"inc {arg}"
            case ("jnz", arg1, arg2):
                newinstr=f"cpy {arg1} {arg2}"
            case (_, arg1, arg2):
                newinstr=f"jnz {arg1} {arg2}"
            case _:
                newinstr=oldinstr
        self.instructions[self.pointer+offset]=newinstr
        self.optimize()
        if debug:
            print(f"toggle instruction at {arg} {offset} from {oldinstr} to {newinstr}")
            #print(self.instructions)

    def run(self, debug=False) -> None:
        while self.pointer<len(self.instructions):
            cmd=self.instructions[self.pointer].split()
            if (debug): print(self)
            self.pointer+=1  # will have to decrease by 1 for jumps
            match cmd:
                case ["nop"]:
                    pass
                case ("cpy", arg, target):
                    self.register[target]=self.get(arg)
                case ("inc", arg):
                    self.register[arg]+=1
                case ("mul", arg1, arg2, arg3):
                    self.register[arg3]+=self.get(arg1)*self.get(arg2)
                case ("tgl", arg):
                    self.toggle(arg, debug=debug)
                case ("dec", arg):
                    self.register[arg]-=1
                case ("jnz", testval, offset):
                    self.pointer += self.get(offset) -1 if self.get(testval)!=0 else 0
                case _: raise ValueError(cmd)
        


computer=Computer(INPUTFILE)
computer.register["a"]=7
computer.run(debug=False)
print("Part 1, register A: ",computer.register["a"])

computer=Computer(INPUTFILE)
computer.register["a"]=12
computer.run(debug=False)
print("Part 2, register A: ",computer.register["a"])
