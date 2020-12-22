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
    for i in range(1, len(tests), 2):
        count, test = tests[i-1], tests[i]
        paras = 0
        for j in range(len(test)-1, -1, -1):
            if test[j] == ')': paras += 1
            else: break
        if paras > int(count) // 2: print("Yes")
        else: print("No")
main()