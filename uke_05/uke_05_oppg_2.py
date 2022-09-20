from uib_inf100_graphics import *

def redraw_all(app, canvas): #Island in the sun!
    #BG
    canvas.create_rectangle(0, 0, app.width, app.height, fill='lightblue', outline='black')
    #FG
    canvas.create_rectangle(0, app.height*0.75, app.width, app.height, fill='cyan', outline='black')
    canvas.create_oval(app.width*0.25, app.height*0.6, app.width*0.75, app.height*1.5, fill='orange', outline='black')
    canvas.create_oval(-app.width*0.2, -app.height*0.2, app.height*0.2, app.height*0.2, fill='yellow', outline='black')
    canvas.create_rectangle(app.width*0.49, app.height*0.1, app.width*0.51, app.height*0.6, fill='brown', outline='black')
    canvas.create_polygon(app.width*0.4, app.height*0.15, app.width*0.49, app.height*0.1, app.width*0.49, app.height*0.2, fill='green', outline='black')
    canvas.create_text(app.width*0.5, app.height*0.9, text='Island in the sun!', fill='black', font='Arial')

run_app(width=400, height=200)
