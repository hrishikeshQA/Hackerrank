#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    index = []
    brr = sorted(arr)
    for i in range(len(arr)):
        if not arr[i] == brr[i]:
            index.append(i)
    if len(index) == 0:
        print('yes')
    elif len(index) == 2:
        print('yes')
        print('swap ' + str(index[0]+1) + ' ' + str(index[1]+1))
    else:
        crr=[arr[i] for i in reversed(index)]
        if sorted(crr) == crr:
            print('yes')
            print('reverse ' + str(index[0]+1) + ' ' + str(index[-1]+1))
        else:
            print('no')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
