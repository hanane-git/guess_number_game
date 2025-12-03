from tkinter import *
from tkinter import messagebox
import random

secret_number=random.randint(1,100)
attempts=0

def check_guess():
    global attempts
    try:
        guess=int(entry.get())
        attempts+=1
        if guess<secret_number:
            messagebox.showinfo("Result",f"Guess a higher number\n{10-attempts} Remains")
        elif guess<secret_number:
            messagebox.showinfo("Result",f"Guess a lower number\n{10-attempts} Remains")
        else:
            messagebox.showinfo("Congrats", "You Won")

        if attempts>=10:
            messagebox.showinfo("Result","You Lost")
    except:
        messagebox.showerror("Error","Enter a number")


screen=Tk()
screen.title("Guess Number")
screen.geometry("300x200")

label=Label(screen, text="Guess A Number between 1 and 100")
label.place(relx=0.2, rely=0.2)

entry=Entry(screen)
entry.place(relx=0.3, rely=0.35)

button=Button(screen, text="Guess", command=check_guess)
button.place(relx=0.45,rely=0.5)

screen.mainloop()