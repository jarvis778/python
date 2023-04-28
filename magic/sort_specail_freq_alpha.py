#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter(s)

    ma = {}

    for k, v in c.items():
        ma[k] = v
    '''    
    fre = al 

    '''

    ma = sorted(ma.items(), key=lambda x: (-x[1], x[0]))[0:3]
    # ma.sort(key=lambda x:x[1])
    for i in ma:
        print(i[0], i[1])
    # print(ma)

