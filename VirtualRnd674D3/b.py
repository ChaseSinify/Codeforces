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
    i = 0

    # while we still have test cases
    while i < len(tests):
        ok = False
        tiles, size = map(int, tests[i].split())
        i += 1 # increment since we read the input

        # # get the tiles
        for j in range(i, i+(2*tiles), 2):
            a,b = map(int, tests[j].split())
            c,d = map(int, tests[j+1].split())
            if (b == c) and (size % 2 == 0):
                ok = True
        if ok: print("YES")
        else: print("NO")
        i += (tiles*2)

main()