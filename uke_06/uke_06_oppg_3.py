def median(numList):
    numListSorted = sorted(numList)
    if len(numListSorted) % 2 != 0:
        median = numListSorted[len(numListSorted)//2]
    else:
        median = (numListSorted[(len(numListSorted)//2)-1] + numListSorted[len(numListSorted)//2])/2
    
    return median

print("Tester median... ", end="")
assert(3 == median([1, 2, 3, 6, 7]))
assert(3.5 == median([1, 2, 3, 4, 6, 9]))
a = [-10, 100, 8, 7, 2]
assert(7 == median(a))
assert([-10, 100, 8, 7, 2] == a) # Sjekker at funksjonen ikke er destruktiv
print("OK")
