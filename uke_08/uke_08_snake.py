from uib_inf100_graphics import *
from random import randint

def app_started(app):
    app.debug_mode = True
    app.start_size = 3
    app.snake_size = app.start_size
    app.direction = "east"
    rows = 10
    cols = 10
    app.board = generate_board(app, rows, cols)
    app.head_pos = (rows // 2, app.snake_size)
    app.apple_pos = spawn_apple(app)
    app.active = True
    app.start_timer_delay = 500 #ms
    app.timer_delay = app.start_timer_delay
    app.difficulty = "medium"
    app.difficulty_mod = {
        "easy":{"speed_mod":1, "max_speed":300, "color":"green"},
        "medium":{"speed_mod":2, "max_speed":200, "color":"orange"},
        "hard":{"speed_mod":3, "max_speed":150, "color":"red"},
    }

def generate_board(app, row_count, col_count):
    board = []
    for i in range(row_count):
        row = []
        for j in range(col_count):
            if i == row_count // 2 and j <= app.snake_size: 
                row.append(j)
            else:
                row.append(0)
        board.append(row)
    return board

def timer_fired(app):
    if app.active and not app.debug_mode:
        move_snake(app)

def key_pressed(app, event):
    if app.active:
        if (event.key == "w" or event.key == "Up") and app.direction != "south": #Both WASD and arrow inputs, + checks that you can only turn 90*
            app.direction = "north"
        elif (event.key == "d" or event.key == "Right") and app.direction != "west":
            app.direction = "east"
        elif (event.key == "s" or event.key == "Down") and app.direction != "north":
            app.direction = "south"
        elif (event.key == "a" or event.key == "Left") and app.direction != "east":
            app.direction = "west"
        elif (event.key == "Space"):
            move_snake(app)
    if event.key == "r":
        run_app(width=500, height=400, title="Snake")
    elif event.key == "|":
        app.debug_mode = not app.debug_mode
    elif event.key == "1":
        app.difficulty = "easy"
    elif event.key == "2":
        app.difficulty = "medium"
    elif event.key == "3":
        app.difficulty = "hard"

def redraw_all(app, canvas):
    if app.active: #Default
        draw_board(app, canvas, 25, 25, app.width-25, app.height-25, app.board, app.debug_mode)
        canvas.create_text( #Display Score
                app.width/2,
                10, 
                text=f"Score: {app.snake_size - app.start_size}",
                fill = "black",
                font = "Times 20 bold"
            )
        canvas.create_text( #Display Difficulty
                35,
                10, 
                text=app.difficulty,
                fill = app.difficulty_mod[app.difficulty]["color"],
                font = "Times 15 bold"
            )
        if app.debug_mode:
            canvas.create_text( #Display variables
                app.width/2,  
                app.height - 10, 
                text=f"{app.head_pos=} {app.apple_pos=} {app.direction=} {app.timer_delay=}"
            )
    else: #Game Over
        canvas.create_rectangle( #BG
            25,
            25,
            app.width-25,
            app.height-25,
            fill = "red",
            width = 0
        )
        canvas.create_text( #Game Over
            app.width/2,  
            app.height * 0.4, 
            text = "Game Over",
            fill = "white",
            font = "Times 50 bold"
        )
        canvas.create_text( #Score
            app.width/2,  
            app.height * 0.6, 
            text = f"Final score: {app.snake_size - 3}",
            fill = "white",
            font = "Times 30 bold"
        )
        canvas.create_text( #Restart
            app.width/2,  
            app.height * 0.8, 
            text = "- Press R to restart -",
            fill = "white",
            font = "Times 20 bold"
        )

def draw_board(app, canvas, x1, y1, x2, y2, board, debug_mode):
    height = (y2 - y1) / len(board)
    for i, row in enumerate(board):
        width = (x2 - x1) / len(row)
        for j, cell in enumerate(row):
            #BG
            cell_fill = "#6ee96e" #Lighter green
            if (i + j) % 2 == 0: #BG Alt
                cell_fill = "#5de65d" #Light green
            if cell > 0 and cell != app.snake_size: #Snake Base
                cell_fill = "#ff8c00" #Dark orange
                if (i + j) % 2 == 0 and app.snake_size > 3: #Snake Alt
                    cell_fill = "#ff981a" #orange
            elif cell == app.snake_size: #Snake head
                cell_fill = "#cc7000" #Darkest orange
            elif cell < 0: #Apple
                cell_fill = "red" 

            canvas.create_rectangle( #Display cell
                width * j + x1,
                height * i + y1,
                width * j + width + x1,
                height * i + height + y1,
                fill = cell_fill,
                width = 0
            )

            #Debug per cell
            if debug_mode:
                canvas.create_text( #Display cell coordinates
                width * j + x1 + width * 0.5,  
                height * i + y1 + height * 0.25, 
                text=f"{i},{j}")

                canvas.create_text( #Display cell value
                width * j + x1 + width * 0.5, 
                height * i + y1 + height * 0.75, 
                text=cell)

def move_snake(app):
    app.head_pos = get_next_head_position(app.head_pos[0], app.head_pos[1], app.direction)
    if is_legal(app):
        if app.board[app.head_pos[0]][app.head_pos[1]] == -1: #Check if head at apple
            app.snake_size += 1
            app.apple_pos = spawn_apple(app)
            if app.timer_delay > app.difficulty_mod[app.difficulty]["max_speed"]: #Check if at max speed
                app.timer_delay = app.start_timer_delay - ((app.snake_size) * app.difficulty_mod[app.difficulty]["speed_mod"] * len(app.board)) #Linear delay decrease based on difficulty and boardsize
            else:
                app.timer_delay = app.difficulty_mod[app.difficulty]["max_speed"] #Set to max if above max
        else:
            decrement_board(app)
        app.board[app.head_pos[0]][app.head_pos[1]] = app.snake_size

def decrement_board(app):
    for y, row in enumerate(app.board):
        for x, cell in enumerate(row):
            if cell > 0:
                app.board[y][x] = cell - 1

def spawn_apple(app):
    apple_cords = (randint(0, len(app.board) - 1),randint(0, len(app.board[0]) - 1))
    while app.board[apple_cords[0]][apple_cords[1]] > 0 or app.board[apple_cords[0]][apple_cords[1]] == app.head_pos :
        apple_cords = (randint(0, len(app.board) - 1),randint(0, len(app.board[0]) - 1))
    app.board[apple_cords[0]][apple_cords[1]] = -1
    return apple_cords

def get_next_head_position(head_row, head_col, direction):
    directions = {
        "north":(head_row - 1, head_col),
        "south":(head_row + 1, head_col),
        "east":(head_row, head_col + 1),
        "west":(head_row, head_col - 1),
    }
    return directions[direction]

def is_legal(app):
    if len(app.board) - 1 < app.head_pos[0] or app.head_pos[0] < 0 or len(app.board[0]) - 1 < app.head_pos[1] or app.head_pos[1] < 0:
        app.active = False
    elif app.board[app.head_pos[0]][app.head_pos[1]] > 0:
        app.active = False
    return app.active

run_app(width=500, height=400, title="Snake")
