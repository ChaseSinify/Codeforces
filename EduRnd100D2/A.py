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
    lines = lines[1:]
    for line in lines:
        line = [int(x) for x in line.split()]
        summy = sum(line)
        if summy % 9 == 0 and summy // 9 <= min(line):
            print("YES")
        else:
            print("NO")

main()