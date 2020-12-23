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
    vals = {1: 1, 2: 3, 3: 6, 4: 10}
    for test in tests:
        print((((int(test[0])-1))*10)+vals[len(test)])
main()