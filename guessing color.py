import tkinter as tk
import random

colors = ['Red', 'Blue', 'Green', 'Pink', 'Orange', 'Yellow', 'Purple', 'Brown', 'Black', 'White']
score = 0
timeleft = 30

def startGame(event=None):
    if timeleft == 30:
        countdown()
    nextColor()

def nextColor():
    global score
    global timeleft

    if timeleft > 0:
        entry.focus_set()
        if entry.get().lower() == colors[1].lower():
            score += 1
        entry.delete(0, tk.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

# GUI setup
root = tk.Tk()
root.title("Color Guessing Game")
root.geometry("400x200")

instructions = tk.Label(root, text="Type the color of the words displayed—not the word itself!", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tk.Label(root, text="Score: 0", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tk.Label(root, text="Time left: 30", font=('Helvetica', 12))
timeLabel.pack()

label = tk.Label(root, font=('Helvetica', 40))
label.pack()

entry = tk.Entry(root)
entry.pack()
entry.bind('<Return>', startGame)

entry.focus_set()
root.mainloop()

