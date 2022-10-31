def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def collect_collatz(a, b):
    collatz_dict = {}
    for i in range(a, b):
        collatz_dict[i] = collatz_sequence(i)
    return collatz_dict

print("Tester collect_collatz... ", end="")
assert({
    1: [1],
    2: [2, 1], 
    3: [3, 10, 5, 16, 8, 4, 2, 1],
} == collect_collatz(1, 4))
assert({
    3: [3, 10, 5, 16, 8, 4, 2, 1],
    4: [4, 2, 1],
    5: [5, 16, 8, 4, 2, 1],
} == collect_collatz(3, 6))
print("OK")

