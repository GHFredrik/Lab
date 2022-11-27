def dot_product(list_a, list_b):
    result = 0
    for i in range(len(list_a)):
        result += list_a[i] * list_b[i]
    return result

print("Tester dot_product... ", end="")
assert(32 == dot_product([1, 2, 3], [4, 5, 6]))
assert(12 == dot_product([0, 6, 1], [400, 1, 6]))
assert(657 == dot_product([43, 6, 1], [15, 1, 6]))
print("OK")
