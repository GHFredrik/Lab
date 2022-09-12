def get_common_symbols(s1, s2):
    common = []
    for chr in s1:
        if chr in s2 and chr not in common:
            common.append(chr)
    return "".join(common)
        

# print("Tester get_common_symbols... ", end="")
# assert("" == get_common_symbols("foo", "bar"))
# assert("fo" == get_common_symbols("foo", "foo"))
# assert("Hvr e,a" == get_common_symbols("Hvor er du, Kari?", 
#                                        "Her er jeg, Olav!"))
# print("OK")