import random
import tkinter as tk
from tkinter import messagebox

"""
    Have a button or a menu option to exit the game.
    Have a button to restart the game - the computer generates a new random number and resets the guess-counter.
    Have a button that will show the currently hidden value in a pop-out dialog.

"""
class GuessNumberGame:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Number Guessing Game")
        self.root.geometry("500x400")

        # Greet user
        self.greet_label = tk.Label(
            self.root,
            text="""Guess a whole number between 1 and 20.
            Press <Enter> or click the <Evaluate> button to check guess."""
        )
        self.greet_label.pack(pady=20)

        # Generate random number and initialize guess count
        self.true_number = random.randint(1, 20)
        self.guess_count = 0
    
        # Create entry box
        self.user_guess = tk.Entry(self.root)
        self.user_guess.bind("<Return>", lambda event: self.evaluate_guess())
        self.user_guess.pack()

        # Create evaluation button
        self.guess_button = tk.Button(self.root, text="Evaluate", command=self.evaluate_guess)
        self.guess_button.pack(pady=10)

        # Show guess count
        self.guess_count_label = tk.Label(self.root, text=f"Guess count: {self.guess_count}")
        self.guess_count_label.pack(pady=10)

        # Show guess result
        self.info_label = tk.Label(self.root, text="New game start.")
        self.info_label.pack(pady=10)

        # Reveal secret number
        self.show_button = tk.Button(self.root, text="Reveal Number", command=self.reveal_number)
        self.show_button.pack(pady=10)

        # Restart button
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart)
        self.restart_button.pack(pady=10)
    
        # Quit button
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

    def evaluate_guess(self):
        try:
            guess = int(self.user_guess.get())
            self.guess_count += 1
            self.guess_count_label.configure(text=f"Guess count: {self.guess_count}")
            
            if guess == self.true_number:
                self.info_label.config(text="Correct.")
                messagebox.showinfo(message=f"You guessed right!\nTotal guess count: {self.guess_count}")
                if messagebox.askyesno(message="Do you want to quit?\nClick Yes to exit or No to restart."):
                    self.quit()
                else:
                    self.restart()
            
            elif guess < self.true_number:
                self.info_label.config(text="Too small. Try again.")
            else:
                self.info_label.config(text="Too large. Try again.")
        except ValueError:
            self.info_label.config(text="Please enter a valid number.")
    
    def reveal_number(self):
        messagebox.showinfo("Cheater's den", f"Number was {self.true_number}.")
        self.info_label.config(text="You chose to cheat.")
        if messagebox.askyesno(message="Do you want to quit?\nClick Yes to exit or No to restart."):
            self.quit()
        else:
            self.restart()
    
    def restart(self):
        self.guess_count = 0
        self.true_number = random.randint(1, 20)
        self.info_label.config(text="New game start.")
        self.guess_count_label.configure(text=f"Guess count: 0")
    
    def quit(self):
        self.root.destroy()

        
if __name__ == "__main__":
    game = GuessNumberGame()
    game.mainloop()

