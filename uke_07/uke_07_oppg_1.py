from uib_inf100_graphics import *

def draw_grid(canvas, x1, y1, x2, y2, color_grid):
    height = (y2 - y1) / len(color_grid)
    for i, row in enumerate(color_grid):
        width = (x2 - x1) / len(row)
        for j, cell in enumerate(row):
            canvas.create_rectangle(
            width * j + x1,
            height * i + y1,
            width * j + width + x1,
            height * i + height + y1,
            fill = cell,
            outline = 'black')

def redraw_all(app, canvas):
    # Et 3x3 rutenett med innebygde farger
    draw_grid(canvas, 50, 20, 130, 100, [
        ["red", "green", "blue"],
        ["yellow", "pink", "cyan"],
        ["black", "gray", "orange"],
    ])

    # Et sjakkbrett
    draw_grid(canvas, 150, 20, 350, 100, [
        ["white", "black"] * 4,
        ["black", "white"] * 4,
    ] * 4)

    # En 2D-liste med kun én rad
    draw_grid(canvas, 50, 120, 350, 180, [
        ['#00c', '#01c', '#02c', '#03c', '#04c', '#05c', '#06c', '#07c',
         '#08c', '#09c', '#0ac', '#0bc', '#0cc', '#0dc', '#0ec', '#0fc']
    ])

run_app(width=400, height=200)