import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os
import sys

def main():
    tests = [x.strip() for x in sys.stdin.readlines()]
    for i in range(1, len(tests)):
        l, r = (int(x) for x in tests[i].split())
        if 2*l <= r: print(l, 2*l)
        else: print(-1, -1)
main()