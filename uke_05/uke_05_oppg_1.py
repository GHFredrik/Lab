#1A

def remove_threes(numList):
    while 3 in numList:
            numList.remove(3)
    return numList

# print("Tester remove_threes... ", end="")
# # Test 1
# a = [1, 2, 3, 4]
# remove_threes(a)
# assert(a == [1, 2, 4])

# # Test 2
# a = [1, 2, 3, 3]
# remove_threes(a)
# assert(a == [1, 2])

# # Test 3
# a = [3, 3, 1, 3, 2, 4, 3, 3, 3]
# remove_threes(a)
# assert(a == [1, 2, 4])

# # Test 4
# a = [3, 3]
# remove_threes(a)
# assert(a == [])
# print("OK")

#1B

def every_fourth(list):
    newList = []
    for i in range(0, len(list), 4):
        newList.append(list[i])
    return newList

# print("Tester every_fourth... ", end="")
# # Test 1
# a = ["a", "b", "c", "d", "e"]
# assert(["a", "e"] == every_fourth(a))
# assert(["a", "b", "c", "d", "e"] == a)

# # Test 2
# a = list(range(10))
# assert([0, 4, 8] == every_fourth(a))
# assert(list(range(10)) == a)

# # Test 3
# a = list(range(20, 1000))
# assert(list(range(20, 1000, 4)) == every_fourth(a))
# assert(list(range(20, 1000)) == a)
# print("OK")

#1C

def halve_values(numList):
    for i in range(len(numList)):
        numList[i] = numList[i] / 2
    return numList

# print("Tester halve_values... ", end="")
# a = [1, 2, 3]
# halve_values(a)
# assert([0.5, 1, 1.5] == a)
# print("OK")

#1D

def unique_values(list):
    newList = []
    for entry in list:
        if entry not in newList:
            newList.append(entry)
    return newList

# print("Tester unique_values... ", end="")
# # Test 1
# a = [1, 1, 2, 1, 3, 3, 3, 2]
# assert([1, 2, 3] == unique_values(a))
# assert([1, 1, 2, 1, 3, 3, 3, 2] == a)

# # Test 2
# a = ["a", "b", "c"]
# assert(["a", "b", "c"] == unique_values(a))
# assert(["a", "b", "c"] == a)
# print("OK")

#1E

def add_list(numList, addList):
    for i in range(len(numList)):
        numList[i] = numList[i] + addList[i]
    return numList

# print("Tester add_list... ", end="")
# a = [1, 2, 3]
# b = [4, 2, -3]
# add_list(a, b)
# assert([5, 4, 0] == a)
# assert([4, 2, -3] == b)
# print("OK")

