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
    count = lines[0]
    words = lines[1:]
    for word in words:
        if len(word) > 10:
            print(word[0] + str(len(word[1:-1])) + word[-1])
        else:
            print(word)
main()
    