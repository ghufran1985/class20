from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title('Rock Paper Scissors')
root.configure(bg='light blue')
root.geometry('400x300')

label1 = Label(root, text="Welcome to Rock Paper Scissors!", bg='light blue')
label1.pack(pady=10)

def start():
    MsgBox = messagebox.askquestion("Start Game", "Do you want to play Rock Paper Scissors?")
    if MsgBox == 'yes':
        window()

button1 = Button(root, text="Play Now", command=start, bg='brown', fg='white', relief=RAISED, bd=5)
button1.pack(pady=10)

def window():
    top = Toplevel()
    top.title("Rock Paper Scissors")
    top.configure(bg='light grey')
    top.geometry("400x250")

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    def play(choice):
        computer_choice = random.randint(1, 3)
        result = winner(choice, computer_choice)
        messagebox.showinfo("Result", f"You chose {choices[choice]}\nComputer chose {choices[computer_choice]}\n\n{result}")

    def winner(player, computer):
        conditions = {
            1: 3,
            2: 1,
            3: 2
        }

        if player == computer:
            return "It's a tie!"
        if conditions[player] == computer:
            return "You win! "
        return "You lose! "

    Label(top, text="Choose your move:", bg='light grey').pack(pady=10)
    Button(top, text="Rock", command=lambda: play(1)).pack(pady=5)
    Button(top, text="Paper", command=lambda: play(2)).pack(pady=5)
    Button(top, text="Scissors", command=lambda: play(3)).pack(pady=5)

    top.mainloop()

root.mainloop()