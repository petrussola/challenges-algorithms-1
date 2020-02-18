from data import test
import sys


def rec_search(list, low, high, target):
    while low <= high:
        middle = (low + high) // 2
        if list[middle] == target:
            return middle
        elif list[middle] > target:
            high = middle - 1
            return rec_search(list, low, high, target)
        else:
            low = middle + 1
            return rec_search(list, low, high, target)
    return "Not found"


print(rec_search(test, 0, len(test) - 1, int(sys.argv[1])))
