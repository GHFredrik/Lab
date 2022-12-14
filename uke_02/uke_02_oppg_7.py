def is_legal_triangle(s1, s2, s3):
    sides = [s1, s2, s3]
    high = max(sides)
    sides.remove(high)
    try:
        if sides[0] + sides[1] > high:
            return True
        else:
            return False
    except TypeError:
        return False

print(is_legal_triangle(2, 2, 3))
print(is_legal_triangle(3, 2, 1))
print(is_legal_triangle("2", "2", "3"))