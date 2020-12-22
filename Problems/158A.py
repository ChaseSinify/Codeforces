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
    n,k = (int(x) for x in lines[0].split())
    scores = [int(x) for x in lines[1].split()]
    print(sum([1 for score in scores if score >= scores[k-1] and score > 0]))

main()