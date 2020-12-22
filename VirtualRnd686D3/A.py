import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os
import sys
def main():
    lines = [int(x.strip()) for x in sys.stdin.readlines()][1:]
    for n in lines:
        temp = [x for x in range(n, 0, -1)]
        if len(temp) > 2:
            temp[0], temp[len(temp) // 2] = temp[len(temp) // 2], temp[0]
        print(*temp)
    
main()