def pyramad(rounds):
    list = []
    for i in range(rounds):
        list.append((2 + i) * (rounds - i))
    return list

print(pyramad(10))