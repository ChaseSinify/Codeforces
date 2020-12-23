import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os
import sys

def main():
    n = [int(x.strip()) for x in sys.stdin.readlines()][0]
    x, y, res = 0, 0, 0
    if n % 2 == 1:
        x = 1
        for _ in range(1, n+1, 2):
            x += 1
            y += 1
        res = 2 * x * y
    else:
        x, y = 1, 1
        for _ in range(1, n+1, 2):
            x += 1
            y += 1
        res = x * y
    print(res)
    
main()