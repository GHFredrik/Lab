def find_nth_occurence(src, schr, n): #src = source string, schr = search character
    occs = 0 # occurences
    for i in range(len(src)):
        if src[i] == schr:
            occs += 1
        if occs == n:
            return (i)
    return(-1)
        

print("Tester find_nth_occurence... ", end="")
assert(0 == find_nth_occurence("abcabc", "a", 1))
assert(2 == find_nth_occurence("abcabc", "c", 1))
assert(-1 == find_nth_occurence("abcabc", "x", 1))
assert(3 == find_nth_occurence("abcabc", "a", 2))
assert(5 == find_nth_occurence("abcabc", "c", 2))
assert(-1 == find_nth_occurence("abcab", "c", 2))
print("OK")