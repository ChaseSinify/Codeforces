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
    cases = lines[1]
    tests = lines[1:]
    i = 0
    while i < len(tests) - 1: # exit once we go outside of input test cases
        boardSize, rooks = tests[i].split()
        moves = 0
        pos = set()
        ref = 0
        # get each of the rook pos
        for j in range(i+1, i + int(rooks) + 1):
            x,y = tests[j].split()
            if x != y:
                ref += 2
                pos.add(x)
                pos.add(y)
                moves += 1
        if len(pos) + 1 < ref:
            moves += 1
        
        i += 1 + int(rooks) # 1 is normal step, m is how many rows are same case
        print(moves)
main()