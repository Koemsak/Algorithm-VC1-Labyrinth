import tkinter as tk
import random



root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry('1200x550')
root.title('Pacman game')
canvas = tk.Canvas(root)
#VARIABLE
#-----------------------------*CREATE GRID OF GAME*---------------------------------------
countCoins = 0
notFinished = True
notWin = True
choiceToMove = []
indexOfPlayer = []

canvas = tk.Canvas(root, bg='#455a64')

grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 1],
    [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
    [1, 2, 2, 4, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 4, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
]

#--------------*NUMBER 0 IS NOTHING*--------------------------#
#--------------*NUMBER 1 IS WALLS*----------------------------#
#--------------*NUMBER 2 IS COINS*----------------------------#
#--------------*NUMBER 3 IS PLAYER*---------------------------#
#--------------*NUMBER 4 IS ENEMIES*--------------------------#


#-----------------------------*CREATE FUNCTION TO DRAW GIRD*---------------------------------------

def  mySquare():
    global myScore, enemy, pacMan
    myScore = 'SCORE: ' + str(countCoins)
    for row in range(len(grid)):
        for  col in  range(len(grid[row])):
            x1 = 50*col + 125
            y1 = 50*row + 50
            x2 = 50+x1
            y2 = 50+y1
            if grid[row][col] == 0:
                canvas.create_rectangle(x1, y1, x2, y2, fill='', outline='')
            elif grid[row][col] == 1:
                # canvas.create_rectangle(x1, y1, x2, y2, fill="")
                myBg = canvas.create_image(x1, y1, image=wall, anchor="nw")
            elif  grid[row][col] == 2:
                coins = canvas.create_image(x1+15, y1+15,image=myCoin, anchor='nw')
            elif grid[row][col] == 3:
                pacMan = canvas.create_image(x1, y1, image=myPac, anchor='nw')
            elif grid[row][col] == 4:
                enemy = canvas.create_image(x1, y1, image=theEnemy,anchor='nw')
    canvas.create_text(250, 25, text=myScore, font=('consolas', 24, 'bold'), fill='#e0e0e0')


#-----------------------------*FUNCTION TO FIND INDEX OF PLAYER*---------------------------------------

def indexOfPac(grid):
    global indexOfPlayer
    for index1 in range(len(grid)):
        for index2 in range(len(grid[index1])):
            if grid[index1][index2] == 3:
                indexOfPlayer = [index1, index2]
    return indexOfPlayer


#-----------------------------*END GAME WITH RESULT LOST (GAME OVER) AND WIN*---------------------------------------

def clean():
    global grid
    grid = []
    mySquare()

def yourScore():
    global countCoins, notFinished
    if not notFinished:
        canvas.delete('all')
        if countCoins != 750:
            canvas.create_image(0, 0, image=overGame, anchor='nw')
            canvas.create_text(600,450, text="Your Score "+str(countCoins), font=(('couriernew'), 38, 'bold'), fill='#2196f3')
        else:
            canvas.create_image(0, 0, image=win, anchor='nw')
            canvas.create_text(600, 470, text="YOU WIN", font=(('consolas'), 48, 'bold'), fill='#b71c1c')


#-----------------------------*FUNCTION TO FIND INDEX OF ENEMY*---------------------------------------
def indexOfEnemy(grid):
    indexEnemy = []
    for index1 in range(len(grid)):
        for  index2 in range(len(grid[index1])):
            if grid[index1][index2] == 4:
                indexEnemy.append([index1, index2])
    return indexEnemy


#-----------------------------*MOVE ENEMY*---------------------------------------

def canMove(grid, r, c):
    global choiceToMove
    choiceToMove = []
    if grid[r][c-1] != 1 and grid[r][c-1] != 4:
        choiceToMove.append('l')
    if grid[r][c+1] != 1 and grid[r][c+1] != 4:
        choiceToMove.append('r')
    if grid[r-1][c] != 1 and grid[r-1][c] != 4:
        choiceToMove.append('u')
    if grid[r+1][c] != 1 and grid[r+1][c] != 4:
        choiceToMove.append('d')
    return choiceToMove

def moveEnemy():
    global grid, choiceToMove, notFinished
    enemiesIndex = indexOfEnemy(grid)
    for enemyIndex in enemiesIndex:   
        rIndex = enemyIndex[0]
        cIndex = enemyIndex[1]
        whereToMove = canMove(grid, rIndex, cIndex)
        if len(whereToMove) > 0:
            toMove = random.choice(whereToMove)
            if toMove == 'u':
                if grid[rIndex-1][cIndex] == 3:
                    notFinished = False
                elif grid[rIndex-1][cIndex] != 3 and grid[rIndex-1][cIndex] == 0:
                    grid[rIndex-1][cIndex] = 4
                    grid[rIndex][cIndex] = 0
                elif grid[rIndex-1][cIndex] != 3 and grid[rIndex-1][cIndex] == 2:
                    grid[rIndex-1][cIndex] = 4
                    grid[rIndex][cIndex] = 2
            if toMove == 'r':
                if grid[rIndex][cIndex+1] == 3:
                    notFinished = False
                elif grid[rIndex][cIndex+1] != 3 and grid[rIndex][cIndex+1] == 0:
                    grid[rIndex][cIndex+1] = 4
                    grid[rIndex][cIndex] = 0
                elif grid[rIndex][cIndex+1] != 3 and grid[rIndex][cIndex+1] == 2:
                    grid[rIndex][cIndex+1] = 4
                    grid[rIndex][cIndex] = 2
            if toMove == 'd':
                if grid[rIndex+1][cIndex] == 3:
                    notFinished = False
                elif grid[rIndex+1][cIndex] != 3 and grid[rIndex+1][cIndex] == 0 :
                    grid[rIndex+1][cIndex] = 4
                    grid[rIndex][cIndex] = 0
                elif grid[rIndex+1][cIndex] != 3 and grid[rIndex+1][cIndex] == 2 :
                    grid[rIndex+1][cIndex] = 4
                    grid[rIndex][cIndex] = 2
            if toMove == 'l':
                if grid[rIndex][cIndex-1] == 3:
                    notFinished = False
                elif grid[rIndex][cIndex-1] != 3 and grid[rIndex][cIndex-1] == 0 :
                    grid[rIndex][cIndex-1] = 4
                    grid[rIndex][cIndex] = 0
                elif grid[rIndex][cIndex-1] != 3 and grid[rIndex][cIndex-1] == 2  :
                    grid[rIndex][cIndex-1] = 4
                    grid[rIndex][cIndex] = 2

    canvas.delete('all')
    mySquare()
    canvas.after(400, moveEnemy)
    if not notFinished:
        clean()
        yourScore()


#--------------*NUMBER 0 IS NOTHING*--------------------------#
#--------------*NUMBER 1 IS WALLS*----------------------------#
#--------------*NUMBER 2 IS COINS*----------------------------#
#--------------*NUMBER 3 IS PLAYER*---------------------------#
#--------------*NUMBER 4 IS ENEMIES*--------------------------#




#-----------------------------*FUNCTION TO MOVE PACMAN TO LEFT POSITION*---------------------------------------

def moveLeft(event):
    global grid, countCoins, notFinished, notWin
    numOfIndex = indexOfPac(grid)
    rowNum = numOfIndex[0]
    colNum = numOfIndex[1]

    if notFinished:
        if grid[rowNum][colNum-1] != 1:
            grid[rowNum][colNum] = 0
            if grid[rowNum][colNum-1] == 2:
                countCoins += 10
            if grid[rowNum][colNum-1] == 4:
                notFinished = False
                clean()
            if notFinished:
                grid[rowNum][colNum-1] = 3
            if countCoins ==  750:
                notFinished = False
                clean()

    canvas.delete('all')
    mySquare()
    yourScore()
    



#-----------------------------*FUNTCTION TO MOVE PACMAN TO RIGHT POSITION*---------------------------------------

def moveRight(event):
    global grid, countCoins, notFinished,notWin
    numOfIndex = indexOfPac(grid)
    rowNum = numOfIndex[0]
    colNum = numOfIndex[1]
    
    # MOVE LEFT POSITION OF PACMAN

    if notFinished:
        if grid[rowNum][colNum+1] != 1:
            grid[rowNum][colNum] = 0
            if grid[rowNum][colNum+1] == 2:
                countCoins += 10
            if grid[rowNum][colNum+1] == 4:
                notFinished = False
                clean()
            if notFinished:
                grid[rowNum][colNum+1] = 3
            if countCoins ==  750:
                notFinished = False
                clean()

    canvas.delete('all')
    mySquare()
    yourScore()
    


#-----------------------------*FUNCTION TO MOVE PACMAN TO UP POSITION*---------------------------------------

def moveUp(event):
    global grid, countCoins, notFinished, notWin
    numOfIndex = indexOfPac(grid)
    rowNum = numOfIndex[0]
    colNum = numOfIndex[1]

    if notFinished:
        if grid[rowNum-1][colNum] != 1:
            grid[rowNum][colNum] = 0
            if grid[rowNum-1][colNum] == 2:
                countCoins += 10
            if grid[rowNum-1][colNum] == 4:
                notFinished = False
                clean()
            if notFinished:
                grid[rowNum-1][colNum] = 3

            if countCoins ==  750:
                notFinished = False
                clean()

    canvas.delete('all')
    mySquare()
    yourScore()
    
    



#-----------------------------*FUCNTION TO MOVE PACMAN TO DOWN POSITION*---------------------------------------


def moveDown(event):
    global grid, countCoins, notFinished
    numOfIndex = indexOfPac(grid)
    rowNum = numOfIndex[0]
    colNum = numOfIndex[1]

    if notFinished:
        if grid[rowNum+1][colNum] != 1:
            grid[rowNum][colNum] = 0
            if grid[rowNum+1][colNum] == 2:
                countCoins += 10
            if grid[rowNum+1][colNum] == 4:
                notFinished = False
                clean()
            if notFinished:
                grid[rowNum+1][colNum] = 3

            if countCoins ==  750:
                notFinished = False
                clean()

    canvas.delete('all')
    mySquare()
    yourScore()






#-----------------------------*PUT IMAGE TO SHOW ON INTERFACE*---------------------------------------


wall = tk.PhotoImage(file='walls.png')
myCoin = tk.PhotoImage(file='coin.png')
myPac = tk.PhotoImage(file='male.png')
theEnemy = tk.PhotoImage(file='enemy.png')
overGame = tk.PhotoImage(file='over.png')
win = tk.PhotoImage(file='youWin.png')


#-----------------------------*USE KEY LEFT, RIGHT, UP, DOWN TO MOVE PACMAN*---------------------------------------


root.bind("<Left>", moveLeft) # MOVE PLAYER TO LEFT
root.bind("<Right>", moveRight) # MOVE PLAYER TO RIGHT
root.bind("<Up>", moveUp) # MOVE PLAYER TO UP
root.bind("<Down>",moveDown) # MOVE PLAYER TO DOWN




canvas.pack(expand=True, fill='both')


#-----------------------------*CALL FUNCTION*---------------------------------------

mySquare()
moveEnemy()


#-----------------------------*DISPLAY WINDOWS*---------------------------------------
root.mainloop()