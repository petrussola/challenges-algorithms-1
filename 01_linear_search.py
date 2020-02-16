from data import test
import sys


def linear_search(list, item):
    index = 0
    for i in list:
        if i == item:
            return index
        else:
            index += 1
    return "Not found"


print(linear_search(test, int(sys.argv[1])))
