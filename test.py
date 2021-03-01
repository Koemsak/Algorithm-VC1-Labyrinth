import tkinter as tk

#_________________Ball_____________________________

x_speed = 0 
y_speed = 10 

#_________________Size of screen____________________

screenWidth = 600
screenHeight = 600

#_________________Functions to move__________________

def goUp(event):
    global x_speed, y_speed
    y_speed = -10
    x_speed = 0

def goDown(event):
    global x_speed, y_speed
    y_speed = 10
    x_speed = 0

def goLeft(event):
    global x_speed, y_speed
    y_speed = 0
    x_speed = -10

def goRight(event):
    global x_speed, y_speed
    y_speed = 0
    x_speed = 10

def move_oval():
    global x_speed, y_speed
    
    (left_position, top_position, right_position, bottom_position)  = canvas.coords(oval)

    if (right_position >= screenWidth) or (left_position <= 0):
        x_speed = -x_speed

    elif (bottom_position >= screenHeight) or (top_position <= 0):
        y_speed = -y_speed

    canvas.move(oval, x_speed, y_speed)
    canvas.after(50, move_oval)
    

#________________Create an empty window_____________________________________

root = tk.Tk()
root.geometry(str(screenWidth) + 'x' + str(screenHeight))
root.title('Pro-Developer')
root.resizable(False, False)
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

#________________The first oval______________________________________________

oval = canvas.create_oval(270, 270, 330, 330, fill = 'green')

#________________Start moving!________________________________________________

move_oval()

#________________Controll by keys____________________________________________
root.bind('<Up>', goUp)
root.bind('<Down>', goDown)
root.bind('<Right>', goRight)
root.bind('<Left>', goLeft)

root.mainloop()