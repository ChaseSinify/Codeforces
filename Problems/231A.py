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
    print(sum([1 for x in lines if x.count('1') >= 2]))
    
main()