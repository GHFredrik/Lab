def main(change_list, original_price):
    new_price = original_price
    for i in range(len(change_list)):
        new_price = new_price * (100 + change_list[i]) / 100
    return new_price
    
# print(main([50,-50,50,-50,50,-50], 100))

def has_consecutive_elements(a):
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            return True
        else:
            return False

# print(has_consecutive_elements([1, 1, 3, 4]))
# print(has_consecutive_elements([4, 3, 4, 3]))

from uib_inf100_graphics import *

def draw_ladder(app, canvas, steps):
    steps += 1 #Account for missing rung
    spacing = (app.height*0.8)/steps
    for i in range(steps):
        canvas.create_rectangle(
        app.width*0.25,
        app.height*0.1 + spacing * i,
        app.width*0.75, 
        app.height*0.1 + spacing + spacing * i, 
        outline='red', 
        width=5)

    canvas.create_line( #Remove top rung
        app.width*0.20,
        app.height*0.1,
        app.width*0.80, 
        app.height*0.1, 
        fill='white', 
        width=5)

    canvas.create_line( #Remove bottom rung
        app.width*0.20,
        app.height*0.9,
        app.width*0.80, 
        app.height*0.9, 
        fill='white', 
        width=5)

def redraw_all(app, canvas):
    draw_ladder(app, canvas, 6)

run_app(width=400, height=400)