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
    for test in tests:
        target, perFloor = map(int, test.split())
        res = 0

        # if we are on the first floor
        if target <=2: print(1)

        # else, remove the first floor and add 1, 
        # then calculate the amount of 'perfloor' we need to pass
        else:
            target -= 2
            res += 1

            res += math.ceil(target / perFloor)
            print(res)
    
main()