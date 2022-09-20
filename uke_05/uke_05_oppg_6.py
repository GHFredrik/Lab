def non_contigous_substrings(string):
    subList = []
    for i in range(len(string)**2):
        substring = ""
        binary = bin(i)[2:]
        if len(binary) < len(string):
            binary = ((len(string) - len(binary)) * "0" + binary)
        binary = binary.rstrip("0")
        for i in range(len(binary)):
            if binary[i] == "1":
                substring+=string[i]
        subList.append(substring)
    return list(set(subList))

print("Tester non_contigous_substrings... ", end="")
# Test 1
assert(sorted([
  "", # Den tomme strengen er alltid en substreng
  "a", "b", "c", "d",
  "ab", "ac", "ad", "bc", "bd", "cd",
  "abc", "abd", "acd", "bcd",
  "abcd",
]) == sorted(non_contigous_substrings("abcd")))

# Test 2
assert(sorted([
  "",
  "f", "o",  # Merk: "o" opptrer bare én gang
  "fo", "oo",
  "foo",
]) == sorted(non_contigous_substrings("foo")))
print("OK")

#Er jeg et geni, hvorfor fungerte dette?