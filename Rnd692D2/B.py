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
    cases = lines[1]
    tests = lines[1:]
    for test in tests: # for each test
        minny, worked = int(test), False
        while not worked: # while we haven't all div
            worked = True
            digits = [int(x) for x in str(minny)] # get each dig
            for dig in digits: # for each dig -> see if it div
                if dig == 0: continue
                if minny % dig != 0:
                    worked = False
                    break
            if not worked:
                minny += 1
        print(minny)

main()