import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os
import sys

def main():
    lines = [x.strip() for x in sys.stdin.readlines()]
    cases, tests = lines[0], lines[1:]

    for i in range(0, len(tests), 3):
        deckL, red, blue = int(tests[i]), tests[i+1], tests[i+2]
        redDig = [int(x) for x in red]
        blueDig = [int(x) for x in blue]
        res = 0 # if this is > 0, red wins, < 0 blue wins, 0 == tie
        for j in range(deckL):
            if redDig[j] > blueDig[j]: res += 1
            elif redDig[j] < blueDig[j]: res -= 1
        
        if res == 0: print("EQUAL")
        elif res > 0: print("RED")
        elif res < 0: print("BLUE")
main()