import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os
import sys
def main():
    lines = [x.strip() for x in sys.stdin.readlines()][1:]
    for i in range(1, len(lines), 2):
        print(lines[i])
    
main()