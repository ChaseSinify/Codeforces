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
    for i in range(1, len(tests), 2):
        test = [int(x) for x in tests[i].split()]
        maxxy = max(test)
        domIndex = -1
        for j in range(0, len(test)):
            if test[j] != maxxy: continue
            if j > 0 and (test[j-1] != maxxy): domIndex = j + 1
            if j < len(test) - 1 and (test[j + 1] != maxxy): domIndex = j + 1
        print(domIndex)
main()