def sort_by_sign(numList):
    negList = []
    nullList = []
    posList = []
    for num in numList:
        if num > 0:
            posList.append(num)
        elif num < 0:
            negList.append(num)
        elif num == 0:
            nullList.append(num)
    sortedList = negList + nullList + posList
    return sortedList

print("Tester sort_by_sign... ", end="")
# Test 1
a = [3, -4, 1, 0, -1, 0, -2]
assert([-4, -1, -2, 0, 0, 3, 1] == sort_by_sign(a))

# Test 2
a = [10, -10, -2, 0, 0, 30, 10]
assert([-10, -2, 0, 0, 10, 30, 10] ==  sort_by_sign(a))

# Test 3
a = [100, -10, -20, 1000, -1000, 10]
assert([-10, -20, -1000, 100, 1000, 10] == sort_by_sign(a))
print("OK")

