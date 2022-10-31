def word_comparison(w1, w2):
    my_dict = {}
    common = []
    w1_unique = []
    w2_unique = []

    for chr in w1:
        if chr in w2: #Common
            common.append(chr)
        else: #Unique to w1
            w1_unique.append(chr)

    for chr in w2: #Unique to w2
        if chr not in w1:
            w2_unique.append(chr)

    my_dict["In common"] = set(common)
    my_dict["Unique to first word"] = set(w1_unique)
    my_dict["Unique to second word"] = set(w2_unique)

    return my_dict

print("Tester word_comparison... ", end="")
assert({
  "In common": {"e", "c"},
  "Unique to first word": {"r", "u", "t", "p", "o", "m"},
  "Unique to second word": {"s", "i", "n"},
} == word_comparison("computer", "science"))
print("OK")
