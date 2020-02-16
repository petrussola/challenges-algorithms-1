from data import test
import math
import sys


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        middle = math.floor((low + high) / 2)
        if list[middle] == item:
            return middle
        elif list[middle] > item:
            high = middle - 1
        else:
            low = middle + 1
    return "Not found"


print(binary_search(test, int(sys.argv[1])))
