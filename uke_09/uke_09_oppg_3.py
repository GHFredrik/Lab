def rotate(grid):
    rotated_grid = []
    for i in range(len(grid[0])):
        row = []
        for j in range(len(grid)):
            row.append(grid[j][i])
        rotated_grid.append(row)
    return rotated_grid

print("Tester rotate... ", end="")
# Test 1
a = [
    ["a", "c"],
    ["b", "d"]
]
assert([
    ["a", "b"],
    ["c", "d"],
] == rotate(a))

# Test 2
a = [
    [1, 4],
    [2, 5],
    [3, 6],
]
assert([
    [1, 2, 3],
    [4, 5, 6],
] == rotate(a))
# Sjekk at a ikke er mutert
assert([[1, 4], [2, 5], [3, 6]] == a)
print("OK")
