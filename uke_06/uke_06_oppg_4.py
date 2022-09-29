def smallest_absolute_difference(numList):
    numListSorted = sorted(numList)
    smallest = numListSorted[-1]
    for i in range(len(numListSorted) - 1):
        small = numListSorted[i+1] - numListSorted[i]
        if small < smallest:
            smallest = small
    return abs(smallest)
    
print("Tester smallest_absolute_difference... ", end="")
assert(1 == smallest_absolute_difference([1, 20, 4, 19, -5, 99])) # 20-19
assert(6 == smallest_absolute_difference([67, 19, 40, -5, 1])) # 1-(-5)
assert(0 == smallest_absolute_difference([2, 1, 4, 1, 5, 6])) #1-1
a = [50, 40, 70, 33]
assert(7 == smallest_absolute_difference(a))
assert([50, 40, 70, 33] == a) # Sjekker at funksjonen ikke er destruktiv
print("OK")
