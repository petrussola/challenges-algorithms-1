def linear_search(list, item):
    index = 0
    for i in list:
        if i == item:
            return index
        else:
            index +=1
    return "Not found"

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(linear_search(test, 15))
