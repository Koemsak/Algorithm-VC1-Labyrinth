import tkinter as tk
import random


root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry('1200x1000')
root.title('Pacman game')
canvas = tk.Canvas(root)
#VARIABLE
#-----------------------------*CREATE GRID OF GAME*---------------------------------------
countCoins = 0
finished = True
choiceToMove = []

grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 4, 1],
    # [1, 2, 1, 1, 2, 1, 2, 1, 1, 0, 1, 1, 2, 1, 2, 1, 1, 2, 1],
    # [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
    # [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
    # [1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1],
    # [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1],
    # [1, 1, 1, 1, 2, 1, 2, 2, 2, 0, 2, 2, 4, 1, 2, 1, 1, 1, 1],
    # [1, 1, 1, 1, 2, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 1, 1, 1],
    # [1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 1],
    # [1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1],
    # [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    # [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 2, 2, 1],
    [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
    [1, 2, 2, 4, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 4, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
]

#-----------------------------*CREATE FUNCTION TO DRAW GIRD*---------------------------------------

def  mySquare():
    global myScore, enemy, finished
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
    canvas.create_text(250, 25, text=myScore, font=('consolas', 24, 'bold'), fill='green')


#-----------------------------*FUNCTION TO FIND INDEX OF 3*---------------------------------------

def movePac(grid):
    for index1 in range(len(grid)):
        for index2 in range(len(grid[index1])):
            if grid[index1][index2] == 3:
                indexOfThree = [index1, index2]
    return indexOfThree

def indexOfEnemy(grid):
    indexEnemy = []
    for index1 in range(len(grid)):
        for  index2 in range(len(grid[index1])):
            if grid[index1][index2] == 4:
                indexEnemy.append([index1, index2])
    return indexEnemy



#-----------------------------*FUNCTION TO MOVE PACMAN TO LEFT POSITION*---------------------------------------

def moveLeft(event):
    global grid, countCoins, finished
    indexOfPlayer = movePac(grid)
    rowOfThree = indexOfPlayer[0]
    colOfThree = indexOfPlayer[1]

    # MOVE LEFT POSITION OF PACMAN

    if grid[rowOfThree][colOfThree-1] == 2:
            countCoins += 10

    if grid[rowOfThree][colOfThree-1] != 1 and grid[rowOfThree][colOfThree-1] != 4:
        grid[rowOfThree][colOfThree] = 0
        grid[rowOfThree][colOfThree-1] = 3
    elif grid[rowOfThree][colOfThree-1] != 1 and grid[rowOfThree][colOfThree-1] == 4:
        finished = False
    
    if finished:
        canvas.delete('all')
        mySquare()
    else:
        endGame()


#-----------------------------*FUNTCTION TO MOVE PACMAN TO RIGHT POSITION*---------------------------------------

def moveRight(event):
    global grid, countCoins, finished
    indexOfThree = movePac(grid)
    rowOfThree = indexOfThree[0]
    colOfThree = indexOfThree[1]
    
    # MOVE LEFT POSITION OF PACMAN
    if grid[rowOfThree][colOfThree+1] == 2:
        countCoins += 10

    if grid[rowOfThree][colOfThree+1] != 1 and grid[rowOfThree][colOfThree+1] != 4:
        grid[rowOfThree][colOfThree] = 0
        grid[rowOfThree][colOfThree+1] = 3
    elif grid[rowOfThree][colOfThree+1] != 1 and grid[rowOfThree][colOfThree+1] == 4:
        finished = False

    if finished:
        canvas.delete('all')
        mySquare()
    else:
        endGame()


#-----------------------------*FUNCTION TO MOVE PACMAN TO UP POSITION*---------------------------------------

def moveUp(event):
    global grid, countCoins, finished
    indexOfThree = movePac(grid)
    rowOfThree = indexOfThree[0]
    colOfThree = indexOfThree[1]


    if grid[rowOfThree-1][colOfThree] == 2:
        countCoins += 10
    
    if grid[rowOfThree-1][colOfThree] != 1:
        grid[rowOfThree][colOfThree] = 0
        grid[rowOfThree-1][colOfThree] = 3
    elif grid[rowOfThree-1][colOfThree] != 1 and grid[rowOfThree-1][colOfThree] == 4:
        finished = False

    if finished:
        canvas.delete('all')
        mySquare()
    else:
        endGame()


#-----------------------------*FUCNTION TO MOVE PACMAN TO DOWN POSITION*---------------------------------------


def moveDown(event):
    global grid, countCoins, finished
    indexOfThree = movePac(grid)
    rowOfThree = indexOfThree[0]
    colOfThree = indexOfThree[1]

    if grid[rowOfThree+1][colOfThree] == 2:
        countCoins += 10

    if grid[rowOfThree+1][colOfThree] != 1 :
        grid[rowOfThree][colOfThree] = 0
        grid[rowOfThree+1][colOfThree] = 3
    elif grid[rowOfThree+1][colOfThree] != 1 and grid[rowOfThree+1][colOfThree] == 4:
        finished = False

    if finished:
        canvas.delete('all')
        mySquare()
    else:
        endGame()

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
    global grid, choiceToMove, finished
    enemiesIndex = indexOfEnemy(grid)
    for enemyIndex in enemiesIndex:   
        rIndex = enemyIndex[0]
        cIndex = enemyIndex[1]
        whereToMove = canMove(grid, rIndex, cIndex)
        if len(whereToMove) > 0:
            toMove = random.choice(whereToMove)
            if toMove == 'u':
                if grid[rIndex-1][cIndex] == 3:
                    finished = False
                elif grid[rIndex-1][cIndex] != 3 and grid[rIndex-1][cIndex] == 0:
                    grid[rIndex-1][cIndex] = 4
                    grid[rIndex][cIndex] = 0
                elif grid[rIndex-1][cIndex] != 3 and grid[rIndex-1][cIndex] == 2:
                    grid[rIndex-1][cIndex] = 4
                    grid[rIndex][cIndex] = 2
            elif toMove == 'r':
                if grid[rIndex][cIndex+1] == 3:
                    finished = False
                elif grid[rIndex][cIndex+1] != 3 and grid[rIndex][cIndex+1] == 0:
                    grid[rIndex][cIndex+1] = 4
                    grid[rIndex][cIndex] = 0
                elif grid[rIndex][cIndex+1] != 3 and grid[rIndex][cIndex+1] == 2:
                    grid[rIndex][cIndex+1] = 4
                    grid[rIndex][cIndex] = 2
            elif toMove == 'd':
                if grid[rIndex+1][cIndex] == 3:
                    finished = False
                elif grid[rIndex+1][cIndex] != 3 and grid[rIndex+1][cIndex] == 0:
                    grid[rIndex+1][cIndex] = 4
                    grid[rIndex][cIndex] = 0
                elif grid[rIndex+1][cIndex] != 3 and grid[rIndex+1][cIndex] == 2:
                    grid[rIndex+1][cIndex] = 4
                    grid[rIndex][cIndex] = 2
            elif toMove == 'l':
                if grid[rIndex][cIndex-1] == 3:
                    finished = False
                elif grid[rIndex][cIndex-1] != 3 and grid[rIndex][cIndex-1] == 0:
                    grid[rIndex][cIndex-1] = 4
                    grid[rIndex][cIndex] = 0
                elif grid[rIndex][cIndex-1] != 3 and grid[rIndex][cIndex-1] == 2:
                    grid[rIndex][cIndex-1] = 4
                    grid[rIndex][cIndex] = 2
    if finished:
        canvas.delete('all')
        mySquare()
        canvas.after(300, moveEnemy)
    else:
        endGame()

#-----------------------------*END GAME WHEN THE GAME LOST*---------------------------------------


def endGame():
    canvas.after(1000, lambda:gameOver())
    canvas.after(1500, lambda:yourScore())
   


def yourScore():
    global countCoins
    canvas.create_text(600, 680, text="Your Score "+str(countCoins), font=(('couriernew'), 38), fill='#e21a06')

def gameOver():
    canvas.delete('all')
    canvas.create_image(0, 0, image=overGame, anchor='nw')

#-----------------------------*END GAME WHEN THE GAME WIN*---------------------------------------

# def scoreToWin():
#     global countCoins, end
#     if countCoins == 670 and not end:
#         canvas.delete('all')
#         canvas.create_image(0, 0, image=win, anchor='nw')
#         canvas.after(800, lambda:youWin())
#     return None
        

# def youWin():
#     canvas.create_text(600, 850, text='YOU WIN', font=(('consolas'), 58), fill='#ec09c4')
#     endGame()



#-----------------------------*PUT IMAGE TO SHOW ON INTERFACE*---------------------------------------

wall = tk.PhotoImage(file='walls.png')
myCoin = tk.PhotoImage(file='coin.png')
myPac = tk.PhotoImage(file='pacman.png')
theEnemy = tk.PhotoImage(file='enemy.png')
overGame = tk.PhotoImage(file='over.png')
win = tk.PhotoImage(file='youWin.png')

#-----------------------------*USE KEY LEFT, RIGHT, UP, DOWN TO MOVE PACMAN*---------------------------------------


root.bind("<Left>", moveLeft) # MOVE PLAYER TO LEFT
root.bind("<Right>", moveRight) # MOVE PLAYER TO RIGHT
root.bind("<Up>", moveUp) # MOVE PLAYER TO UP
root.bind("<Down>",moveDown) # MOVE PLAYER TO DOWN




#-----------------------------*SHOW RESULT ON SCREEN*---------------------------------------

mySquare()
moveEnemy()


canvas.pack(expand=True, fill='both')
root.mainloop()