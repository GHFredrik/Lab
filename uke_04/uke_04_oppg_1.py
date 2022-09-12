def insert_at(src, i, ins):
    return (src[0:i] + ins + src[i:])

print("Tester insert_at... ", end="")
assert("XYabcd" == insert_at("abcd", 0, "XY"))
assert("abXYcd"== insert_at("abcd", 2, "XY"))
assert("abcdXY"== insert_at("abcd", 4, "XY"))
print("OK")