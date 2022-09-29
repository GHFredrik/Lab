def alternate_sign_sum(numList):
    result = 0
    sign = 1 # 1 = +, -1 = -
    for i, num in enumerate(numList):
        result += num * sign
        sign = sign * -1 #Invert sign
    return result

print("Tester alternate_sign_sum... ", end="")
assert(3 == alternate_sign_sum([1, 2, 3, 4, 5]))
assert(30 == alternate_sign_sum([10, 20, 30, 40, 50]))

a = [-10, 20, -30, 40, -50]
assert(-150 == alternate_sign_sum([-10, 20, -30, 40, -50]))
assert([-10, 20, -30, 40, -50] == a) # Sjekker at funksjonen ikke er destruktiv
print("OK")
