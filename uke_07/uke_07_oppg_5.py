def eval_dance():
    dance = []
    for i in range(int(input().split(" ")[0])):
        dance.append(input())
    compressed = []

    for y in range(len(dance[0])):
        col = []
        for x in range(len(dance)):
            col.append(dance[x][y])
        compressed.append(set(col))

    count = 1
    for entry in compressed:
        if entry == {'_'}:
            count += 1
    return count

print(eval_dance())