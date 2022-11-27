from uib_inf100_graphics import *
from random import randint

def app_started(app):
    app.rows = 5
    app.cols = 8
    app.margin = 50
    app.selection = (-1, -1)
    app.click = (-1, -1)
    app.mole_pos = generate_mole_pos(app)
    app.score = 0
    app.timer_delay = 1000#ms
    app.time = 30#seconds
    app.active = False
    app.game_over = False

def timer_fired(app):
    if app.active and not app.game_over:
        if app.time == 0:
            game_over(app)
        else:
            app.time -= 1

def game_over(app):
    app.game_over = True
    app.selection = (-1,-1)

def generate_mole_pos(app):
    return (randint(0, app.rows-1),randint(0, app.cols-1)) #Jeg har bevisst valgt å gi mole muligheten til å dukke opp på samme sted
    
def point_in_grid(app, x, y):
    return ((app.margin <= x <= app.width-app.margin) and
            (app.margin <= y <= app.height-app.margin))

def get_cell(app, x, y):
    if (not point_in_grid(app, x, y)):
        return (-1, -1)
    grid_width  = app.width - 2*app.margin
    grid_height = app.height - 2*app.margin
    cell_width  = grid_width / app.cols
    cell_height = grid_height / app.rows

    row = int((y - app.margin) / cell_height)
    col = int((x - app.margin) / cell_width)

    return (row, col)

def get_cell_bounds(app, row, col):
    grid_width  = app.width - 2*app.margin
    grid_height = app.height - 2*app.margin
    column_width = grid_width / app.cols
    row_height = grid_height / app.rows
    x0 = app.margin + col * column_width
    x1 = app.margin + (col+1) * column_width
    y0 = app.margin + row * row_height
    y1 = app.margin + (row+1) * row_height
    return (x0, y0, x1, y1)

def mouse_pressed(app, event):
    if not app.game_over:
        cell = get_cell(app, event.x, event.y)
        if app.mole_pos == cell: #If clicked on mole
            if not app.active:
                app.active = True
            app.mole_pos = generate_mole_pos(app)
            app.score += 1
        elif not (-1,-1) == cell: #If missed mole
            if not app.score <= 0:
                app.score -= 1 #La til dette for å gjøre spillet mer gøy

def mouse_moved(app, event):
    if not app.game_over:
        app.selection = get_cell(app, event.x, event.y)

def key_pressed(app, event):
    if event.key == "r":
        run_app(width=400, height=300)

def redraw_all(app, canvas):
    if not app.game_over:
        canvas.create_text( #Score
                app.width * 0.2,  
                app.height * 0.1, 
                text = f"Score: {app.score}",
                fill = "Black",
                font = "Times 15 bold"
            )

        canvas.create_text( #Time
                app.width * 0.8,  
                app.height * 0.1, 
                text = f"{app.time} :Time",
                fill = "Black",
                font = "Times 15 bold"
            )

        for row in range(app.rows):
            for col in range(app.cols):
                (x0, y0, x1, y1) = get_cell_bounds(app, row, col)
                fill = "grey" #Default
                if app.mole_pos == (row, col): #Mole
                    fill = "orange"
                    if (app.selection == (row, col)): #Mole on hover
                        fill = "yellow"
                elif (app.selection == (row, col)): #On hover
                    fill = "lightgrey"
                canvas.create_rectangle(x0, y0, x1, y1, fill=fill)
    else:
        canvas.create_rectangle( #Game over background
            0,
            0,
            app.width,
            app.height,
            fill = "White"
        )

        canvas.create_text( #Final score
                app.width * 0.5,  
                app.height * 0.5, 
                text = f"Final Score: {app.score}",
                fill = "Black",
                font = "Times 40 bold"
            )

        canvas.create_text( #Restart
                app.width * 0.5,  
                app.height * 0.7, 
                text = "- Press R to try again -",
                fill = "Black",
                font = "Times 20 bold"
            )

run_app(width=400, height=300)
