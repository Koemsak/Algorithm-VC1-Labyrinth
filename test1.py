import tkinter as tk


def displayText1():
    canvas.itemconfigure(text1, state='normal')
    canvas.itemconfigure(text2, state='hidden')


def displayText2():
    canvas.itemconfigure(text1, state='hidden')
    canvas.itemconfigure(text2, state='normal')


root = tk.Tk()
canvas = tk.Canvas(root, height=300,  width=300, bg="red")

# Create 2 texts
text1 = canvas.create_text(150, 150, font=("Arial", 40),  text="text 1")
text2 = canvas.create_text(150, 150, font=("Arial", 40),  text="text 2")

# Create buttons
screen1Button = tk.Button(root, text="DIPLAY TEXT 1", command=displayText1)
screen2Button = tk.Button(root, text="DIPLAY TEXT 2", command=displayText2)

displayText1()  # At start up we displqy text1 only


canvas.pack(side="top")
screen1Button.pack(side="left")
screen2Button.pack(side="right")
root.mainloop()