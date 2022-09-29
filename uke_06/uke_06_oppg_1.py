from uib_inf100_graphics import *

def draw_stripes_from_left_edge(app, canvas, colors):
    for i, color in enumerate(colors):
        barWidth = 10
        canvas.create_rectangle(
            barWidth * i,
            0,
            barWidth * i + barWidth,
            app.height,
            fill = color,
            outline = 'black')

def draw_stripes_from_point(canvas, x, y, width, height, colors):
    for i, color in enumerate(colors):
        canvas.create_rectangle(
            width * i + x,
            y,
            width * i + width + x,
            height + y,
            fill = color,
            outline = 'black')

def draw_vertical_stripes_between(canvas, x1, y1, x2, y2, colors):
    width = (x2 - x1) / len(colors)
    height = y2 - y1
    draw_stripes_from_point(canvas, x1, y1, width, height, colors)

# def redraw_all(app, canvas):
#     draw_stripes_from_left_edge(app, canvas, ["green", "yellow", "#0cc"]*4)
#     draw_stripes_from_point(canvas, 50, 50, 50, 100, ["#f00", "#f50", "#f80"])
#     draw_vertical_stripes_between(canvas=canvas, x1=250, y1=10, x2=350, y2=80,
#                                   colors=["red", "#a00", "#500", "black",])

def redraw_all(app, canvas):
    draw_stripes_from_left_edge(app, canvas, ["blue","navy"]*5)
    draw_stripes_from_point(canvas, 30, 90, 50, 100, 
                            ["#0f0", "#0fc", "#0ff", "#0cf"])
    draw_vertical_stripes_between(canvas=canvas, x1=160, y1=10, x2=350, y2=80,
                                  colors=["black", "red", "yellow"])

    margin = 2
    width = 30 + margin
    height = 20 + margin
    x_left = 270
    y_top = 100
    for row in range(3):
        for col in range(4):
            draw_vertical_stripes_between(canvas=canvas,
                x1=(x_left + width*row),
                y1=(y_top + height*col),
                x2=(x_left + width*(row+1) - margin),
                y2=(y_top + height*(col+1) - margin),
                colors=["#0f0", "#0a0", "#050", "black",])
    
run_app(width=400, height=200)
