from copy import deepcopy

def rings():
    input_grid = []
    for i in range(int(input().split(" ")[0])):
        input_grid.append(list(input()))
    
    empty_grid = []
    for i in range(len(input_grid)):
        row = []
        for j in range(len(input_grid[i])):
            row.append(".")
        empty_grid.append(row)


    for i in range(len(input_grid)): #rows
        for j in range(len(input_grid[i])):
            if input_grid[i][j] == "T":
                near = 0
                for k in range(len(input_grid[i])):
                    if 0<=j-k and j+k<len(input_grid[i]):
                        if input_grid[i][j-k] == "T" and input_grid[i][j+k] == "T":
                            near += 1
                        else:
                            break
                    else:
                        break
                empty_grid[i][j] = str(near)

    empty_grid_2 = deepcopy(empty_grid)
    for i in range(len(input_grid)): #cols
        for j in range(len(input_grid[i])):
            if input_grid[i][j] == "T":
                near = 0
                for k in range(len(input_grid)):
                    if 0<=i-k and i+k<len(input_grid):
                        if input_grid[i-k][j] == "T" and input_grid[i+k][j] == "T":
                            near += 1
                        else:
                            break
                    else:
                        break
                empty_grid_2[i][j] = str(near)

    finished_grid = []
    for i in range(len(empty_grid)):
        row = []
        for j in range(len(empty_grid[i])):
            row.append(min(empty_grid[i][j], empty_grid_2[i][j]))
        finished_grid.append(row)
    
    for row in finished_grid:
        print ("." + (".".join(row)))

rings()

input1="""
5 5
.....
.TTT.
.TTT.
.TTTT
..TT.
"""

