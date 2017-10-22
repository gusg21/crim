import time, os, sys
from colorama import *
init(autoreset=True)
from pprint import *

def clear():
    if "nt" in os.name:
        print("Unix only!")
        sys.exit()
    else:
        os.system("clear")

def printat(x, y, char):
    if len(char) != 1:
        raise TypeError
    print("\033[{};{}H".format(8, 9), char)

def get(array, x, y):
    try:
        return array[y][x]
    except IndexError:
        return None

done = False
x = y = 0
mode = "normal"
direction = "r"
DEBUG = "--debug" in sys.argv
AUTO = not "--noauto" in sys.argv
try:
    MEMSIZE = sys.argv[sys.argv.index("--memsize") + 1]
except:
    MEMSIZE = 100
MEMSIZE = int(MEMSIZE)
MEMORY = [0] * MEMSIZE
if "--fast" in sys.argv:
    SLEEP = 0.01
else:
    SLEEP = 0.3
memsetindex = ""
number = ""
ACCUMULATOR = 0
PRINT_MODE_CHARS = ['"', "'"]
try:
    FILENAME = sys.argv[1]
except:
    print("No file!")
    sys.exit(1)
    
with open(FILENAME, 'r') as myfile:
    lines = myfile.read().split("\n")
    max_len = len(max(lines, key=len))
    ARRAY = [list(l.ljust(max_len, ' ')) for l in lines]

while not done:
    char = get(ARRAY, x, y)
    
    if DEBUG:
        clear()
        xx = yy = 0
        for line in ARRAY:
            for c in line:
                if x == xx and y == yy:
                    print(Back.GREEN + Fore.BLACK + c, end="")
                else:
                    print(c, end="")
                xx += 1
            print("\n", end="")
            yy += 1
            xx = 0
        print("Current: [" + char + "]")
        print("Direction: " + direction)
        print("Mode: " + mode)
        if mode == "memset":
            print("Memory Index: [" + memsetindex + "]")
        print("Accumulator: " + str(ACCUMULATOR))
        print("Memory (First 10 Slots):\n" + str(MEMORY[:10])) 
    
    if mode == "normal":
        if char == "^":
            direction = "u"
        elif char == ">":
            direction = "r"
        elif char == "v":
            direction = "d"
        elif char == "<":
            direction = "l"
        
        if char in PRINT_MODE_CHARS:
            mode = "print"
        
        if char == "s":
            mode = "memset"
        
        if char == "l":
            mode = "memload"
        
        if char == "a":
            mode = "accset"
            
        if char == "c":
            ACCUMULATOR = 0
        
        if char == "i":
            ACCUMULATOR += 1
        
        if char == "p":
            print(ACCUMULATOR)
        
        if char == "f":
            ACCUMULATOR = MEMORY[ACCUMULATOR] + MEMORY[ACCUMULATOR + 1]
            
        if char == "r":
            x = y = 0
            continue
        
        if char == "x":
            if ACCUMULATOR < 0:
                direction = "d"
        
        if char == "t":
            mode = "sleep"
        
        if char == "@":
            sys.exit(0)
        
        if char == "+":
            mode = "add"
        if char == "-":
            mode = "sub"
        if char == "*":
            mode = "mul"
        if char == "/":
            mode = "div"
    elif mode == "print":
        if char in PRINT_MODE_CHARS:
            mode = "normal"
        else:
            print(char, end="")
    elif mode == "memset":
        if char != " ":
            memsetindex += char
        else:
            MEMORY[int(memsetindex)] = ACCUMULATOR
            memsetindex = ""
            mode = "normal"
    elif mode == "accset":
        if char != " ":
            memsetindex += char
        else:
            ACCUMULATOR = int(memsetindex)
            memsetindex = ""
            mode = "normal"
    elif mode == "memload":
        if char != " ":
            memsetindex += char
        else:
            ACCUMULATOR = MEMORY[int(memsetindex)]
            memsetindex = ""
            mode = "normal"
    elif mode == "sleep":
        if char != " ":
            number += char
        else:
            time.sleep(int(number) / 1000)
            number = ""
            mode = "normal"
    elif mode == "add":
        if char != " ":
            number += char
        else:
            ACCUMULATOR = ACCUMULATOR + int(number)
            number = ""
            mode = "normal"
    elif mode == "sub":
        if char != " ":
            number += char
        else:
            ACCUMULATOR = ACCUMULATOR - int(number)
            number = ""
            mode = "normal"
    elif mode == "mul":
        if char != " ":
            number += char
        else:
            ACCUMULATOR = ACCUMULATOR * int(number)
            number = ""
            mode = "normal"
    elif mode == "div":
        if char != " ":
            number += char
        else:
            ACCUMULATOR = ACCUMULATOR / int(number)
            number = ""
            mode = "normal"
        
    if direction == "u":
        y -= 1
    elif direction == "r":
        x += 1
    elif direction == "d":
        y += 1
    elif direction == "l":
        x -= 1
    
    if DEBUG:
        if AUTO:
            time.sleep(SLEEP)
        else:
            input()
