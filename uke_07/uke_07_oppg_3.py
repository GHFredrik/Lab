def all_rows_and_cols_equal_sum(grid):
    rowSums = []
    colSums = []

    for row in grid:
        rowSums.append(sum(row))

    for i in range(len(grid[0])):
        colSum = 0
        for j in range(len(grid)):
            colSum += grid[j][i]
        colSums.append(colSum)

    return {rowSums[0]} == set(rowSums) and {colSums[0]} == set(colSums)

print("Tester all_rows_and_cols_equal_sum... ", end="")
# Test 1
assert(all_rows_and_cols_equal_sum([
        [16, 8, 3],     # begge rader summerer til 27
        [2, 10, 15],    # alle kolonner summerer til 18
    ]))
    
# Test 2
assert(not all_rows_and_cols_equal_sum([
        [3, 0, 9],   # rad0 summerer til 12, col0 summerer til 13
        [4, 5, 3],   # rad1 summerer til 12, col1 summerer til 13
        [6, 8, 1],   # rad2 summerer til 15, col2 summerer til 13
    ]))

# Test 3
assert(not all_rows_and_cols_equal_sum([
        [3, 4, 6],   # rad0 summerer til 13, col0 summerer til 12
        [0, 5, 8],   # rad1 summerer til 13, col1 summerer til 12
        [9, 3, 1],   # rad2 summerer til 13, col2 summerer til 15
    ]))

# Test 3
assert (all_rows_and_cols_equal_sum([
        [1, 2, 3, 4], # alle rader og kolonner summerer til 10
        [2, 3, 4, 1],
        [3, 4, 1, 2],
        [4, 1, 2, 3],
    ]))
print("OK")

