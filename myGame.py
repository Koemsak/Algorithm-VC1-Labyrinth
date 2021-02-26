import tkinter as tk
import random


root = tk.Tk()
root.geometry('1200x1000')
root.title('Pacman game')
canvas = tk.Canvas(root)
#VARIABLE
#-----------------------------*CREATE GRID OF GAME*---------------------------------------
countCoins = 0
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 2, 2, 2, 0, 2, 2, 2, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 2, 1, 1, 0, 1, 1, 2, 1, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 2, 2, 1],
    [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
]

#-----------------------------*CREATE FUNCTION TO DRAW GIRD*---------------------------------------

def  mySquare():
    for row in range(len(grid)):
        for  col in  range(len(grid[row])):
            x1 = 50*col + 125
            y1 = 50*row + 50
            x2 = 50+x1
            y2 = 50+y1
            if grid[row][col] == 0:
                canvas.create_rectangle(x1, y1, x2, y2, fill='', outline='')
            elif grid[row][col] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="")
                myBg = canvas.create_image(x1, y1, image=wall, anchor="nw")
            elif  grid[row][col] == 2:
                coins = canvas.create_image(x1+15, y1+15,image=myCoin, anchor='nw')
            elif grid[row][col] == 3:
                canvas.create_image(x1, y1, image=myPac, anchor='nw')
    canvas.create_text(200, 25, text='SCORE: 0', font='consolas 24', fill='blue')


#-----------------------------*FUNCTION TO FIND INDEX OF 3*---------------------------------------

def movePac(grid):
    for index1 in range(len(grid)):
        for index2 in range(len(grid[index1])):
            if grid[index1][index2] == 3:
                indexOfThree = [index1, index2]
    return indexOfThree


#-----------------------------*FUNCTION TO MOVE PACMAN TO LEFT POSITION*---------------------------------------

def moveLeft(event):
    global grid, countCoins
    indexOfThree = movePac(grid)
    rowOfThree = indexOfThree[0]
    colOfThree = indexOfThree[1]

    if grid[rowOfThree][colOfThree-1] == 2:
        countCoins += 10
        print(countCoins)

    if grid[rowOfThree][colOfThree-1] != 1:
        grid[rowOfThree][colOfThree] = 0
        grid[rowOfThree][colOfThree-1] = 3

        
    
    canvas.delete('all')
    mySquare()


#-----------------------------*FUNTCTION TO MOVE PACMAN TO RIGHT POSITION*---------------------------------------

def moveRight(event):
    global grid, countCoins
    indexOfThree = movePac(grid)
    rowOfThree = indexOfThree[0]
    colOfThree = indexOfThree[1]
    
    if grid[rowOfThree][colOfThree+1] == 2:
        countCoins += 10
        print(countCoins)

    if grid[rowOfThree][colOfThree+1] != 1 and colOfThree < len(grid)-1:
        grid[rowOfThree][colOfThree] = 0
        grid[rowOfThree][colOfThree+1] = 3
    
    canvas.delete('all')
    mySquare()


#-----------------------------*FUNCTION TO MOVE PACMAN TO UP POSITION*---------------------------------------

def moveUp(event):
    global grid, countCoins
    indexOfThree = movePac(grid)
    rowOfThree = indexOfThree[0]
    colOfThree = indexOfThree[1]

    if grid[rowOfThree-1][colOfThree] == 2:
        countCoins += 10
        print(countCoins)
    
    if grid[rowOfThree-1][colOfThree] != 1 and rowOfThree > 0:
        grid[rowOfThree][colOfThree] = 0
        grid[rowOfThree-1][colOfThree] = 3

    
    canvas.delete('all')
    mySquare()


#-----------------------------*FUCNTION TO MOVE PACMAN TO DOWN POSITION*---------------------------------------


def moveDown(event):
    global grid, countCoins
    indexOfThree = movePac(grid)
    rowOfThree = indexOfThree[0]
    colOfThree = indexOfThree[1]

    if grid[rowOfThree+1][colOfThree] == 2:
        countCoins += 10
        print(countCoins)
    
    if grid[rowOfThree+1][colOfThree] != 1 and rowOfThree < len(grid)-1:
        grid[rowOfThree][colOfThree] = 0
        grid[rowOfThree+1][colOfThree] = 3
    
    canvas.delete('all')
    mySquare()

#-----------------------------*PUT IMAGE TO SHOW ON INTERFACE*---------------------------------------

wall = tk.PhotoImage(file='walls.png')
myCoin = tk.PhotoImage(file='coin.png')
myPac = tk.PhotoImage(file='pacman.png')


#-----------------------------*USE KEY LEFT, RIGHT, UP, DOWN TO MOVE PACMAN*---------------------------------------

root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
root.bind("<Up>", moveUp)
root.bind("<Down>",moveDown)

mySquare()

canvas.pack(expand=True, fill='both')
root.mainloop()