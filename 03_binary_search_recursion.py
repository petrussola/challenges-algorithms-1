from data import test
import math
import sys


def binary_search(list, low, high, item):
    if low <= high:
        middle = math.floor((low + high) / 2)
        if list[middle] == item:
            return middle
        elif list[middle] > item:
            return binary_search(list, low, middle - 1, item)
        elif list[middle] < item:
            return binary_search(list, middle + 1, high, item)
    else:
        return "Not found"


print(binary_search(test, 0, len(test) - 1, int(sys.argv[1])))
