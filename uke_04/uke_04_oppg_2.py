def rotate_string(s, n):
    if n > len(s):
        n = n - (len(s) * (n // len(s)))
    return (s[n:] + s[0:n])

print("Tester rotate_string... ", end="")
assert(" World!Hello" == rotate_string("Hello World!", 5))
assert("bar" == rotate_string("bar", 0))
assert("arb" == rotate_string("bar", 1))
assert("rba" == rotate_string("bar", 2))
assert("bar" == rotate_string("bar", 3))
assert("arb" == rotate_string("bar", 4))
print("OK")