#  IMPORTS
from tkinter import *

#  CONSTANTS
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

#  VARIABLES
grid = [[0,0,0,1,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]

# squareSize = #choose the appropriate size of the squares

SQUARE_WIDTH = 100
SQUARE_HEIGHT = 100

#  Function

def arrayToDrawing():
    # draw a line with white and black squares using the global array
    global grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                canvas.create_rectangle(col * SQUARE_WIDTH, row * SQUARE_HEIGHT, (col + 1) * SQUARE_WIDTH, (row + 1) * SQUARE_HEIGHT, fill = 'green')
                # canvas.create_image((col * SQUARE_WIDTH)+50, (row * SQUARE_HEIGHT)+50, anchor=CENTER, image=img)
                
            else:
                canvas.create_rectangle(col * SQUARE_WIDTH, row * SQUARE_HEIGHT, (col + 1) * SQUARE_WIDTH, (row + 1) * SQUARE_HEIGHT, fill = 'gray')
    
# To get index of Number one to analyse that can move or not    
def getIndexOfOne(array):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                indexOfOne = [row, col]
    return indexOfOne



# To move left by key 
def onKeyleft(event):
    moveLeft()

# To move right by key
def onKeyRight(event):
    moveRight()

# To move up by key 
def onKeyUp(event):
    moveUp()

# To move down by key
def onKeyDown(event):
    moveDown()



# To move left by button
def moveLeft():
    global grid 
    indexOfOne = getIndexOfOne(grid)
    rowOfOne = indexOfOne[0]
    colOfOne = indexOfOne[1]
    if  colOfOne != 0:
            grid[rowOfOne][colOfOne] = 0
            grid[rowOfOne][colOfOne - 1] = 1

    canvas.delete("all")
    arrayToDrawing()

# To move right by button
def moveRight():
    global grid
    indexOfOne = getIndexOfOne(grid)
    rowOfOne = indexOfOne[0]
    colOfOne = indexOfOne[1]
    if  colOfOne != (len(grid[rowOfOne]) - 1):
            grid[rowOfOne][colOfOne] = 0
            grid[rowOfOne][colOfOne + 1] = 1
    
    canvas.delete("all")
    arrayToDrawing()

    
# To move up by button
def moveUp():
    global grid 
    indexOfOne = getIndexOfOne(grid)
    rowOfOne = indexOfOne[0]
    colOfOne = indexOfOne[1]
    if  rowOfOne != 0:
            grid[rowOfOne][colOfOne] = 0
            grid[rowOfOne - 1][colOfOne] = 1

    canvas.delete("all")
    arrayToDrawing()

# To move down by button 
def moveDown():
    global grid 
    indexOfOne = getIndexOfOne(grid)
    rowOfOne = indexOfOne[0]
    colOfOne = indexOfOne[1]
    if  rowOfOne != (len(grid) - 1):
            grid[rowOfOne][colOfOne] = 0
            grid[rowOfOne + 1][colOfOne] = 1

    canvas.delete("all")
    arrayToDrawing()



# Create a window to display
root = Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.resizable(False, False)
canvas = Canvas(root)


# Buttons to move
# leftButton = tk.Button(root, text ="Move Right", command = moveRight)
# rightButton = tk.Button(root, text ="Move Left", command = moveLeft)
# upButton = tk.Button(root, text ="Move Up", command = moveUp)
# downButton = tk.Button(root, text ="Move Down", command = moveDown)

# Arrow keys to move
root.bind('<Left>', onKeyleft)
root.bind('<Right>', onKeyRight)
root.bind('<Up>', onKeyUp)
root.bind('<Down>', onKeyDown)


canvas.pack(expand=True, fill="both")
# leftButton.pack()
# rightButton.pack()
# upButton.pack()
# downButton.pack()
# img = PhotoImage(file="C:\\Users\\thon.theng\\Desktop\\Python\\Thurs_18_02\\mario2.gif")

arrayToDrawing()
root.mainloop()

