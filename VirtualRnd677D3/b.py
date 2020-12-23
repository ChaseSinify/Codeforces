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
    tests = lines[1:]
    for i in range(1, len(tests), 2):
        res = 0
        test = ''.join(tests[i].strip().split())
        # print(test)
        if test.count('1') <= 1: 
            print(0)
            continue
        first, last = test.find('1'), test.rfind('1')
        for j in range(first+1, last):
            if test[j] == '0': res += 1
        print(res)

    
main()