def mix(s1, s2):
    result = ""
    for i in range(max(len(s1), len(s2))):
        if i < len(s1):
            result += s1[i]
        if i < len(s2):
            result += s2[i]
    return result

# print("Tester mix... ", end="")
# assert("a1b2c3" == mix("abc", "123"))
# assert("1a2b3c"== mix("123", "abc"))
# assert("abc"== mix("abc", ""))
# assert("abc"== mix("", "abc"))
# assert("aAbBcde" ==mix("abcde", "AB"))
# assert("aAbBCDE"== mix("ab", "ABCDE"))
# print("OK")
