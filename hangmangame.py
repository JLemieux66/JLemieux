# import packages
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hangman_db"]
collection = db["game_outcomes"]


# function outside of class instance
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        # allows me to display a name
        if letter == " ":
            display += "  "
        elif letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

image_folder = "HangmanGame"

# game instance
class HangmanGame:
    def __init__(self, master):
        # main root window
        self.master = master
        self.word = self.select_word()
        self.max_attempts = 6
        self.attempts = 0
        self.guessed_letters = []
        # stringvar function adds letters to the display
        self.display = tk.StringVar()

        # main banner of bruins
        self.banner_image = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "banner.png")))
        self.banner = tk.Label(master, image=self.banner_image)
        self.banner.pack(side="top", pady=10)

        # sets size of canvas where we're putting widgets
        self.canvas = tk.Canvas(master, width=900, height=300)  
        self.canvas.pack(side="top", fill="both")

        # opens hangman image, cycles through attempts to update the name of the image which corresponds
        self.images = [ImageTk.PhotoImage(Image.open(os.path.join(image_folder, f"hangman{index}.png")))
                        for index in range(self.max_attempts + 1)]
        self.image_display = self.canvas.create_image(self.canvas.winfo_reqwidth() / 2, self.canvas.winfo_reqheight() / 2, anchor=tk.CENTER, image=self.images[0])

        # display of current state of word
        self.word_display = tk.Label(master, textvariable=self.display, font=("Arial", 24))
        self.word_display.pack(side="top", fill="both", pady=10)

        # textbox for entries
        self.entry = tk.Entry(master, font=("Arial", 16))
        self.entry.pack(side="top", fill="both", pady=10)
        # basically binds the enter key to the guess letter method
        self.entry.bind("<Return>", self.guess_letter)

        # play again button, pack forget allows me to hide it until called
        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(side="top", pady=10)
        self.play_again_button.pack_forget()  

        self.display_word()

    def write_to_file(self, outcome):
        with open("hangman_stats.txt", "a") as file:
            file.write(outcome + "\n")

    def write_to_mongodb(self, outcome):
        game_result = {"outcome": outcome, "word": self.word}
        collection.insert_one(game_result)

    def read_stats_file(self, filename="hangman_stats.txt"):
        try:
            with open(filename, "r") as file:
                stats = file.readlines()
                for stat in stats:
                    print(stat.strip())
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    # method using random to select a name
    def select_word(self):
        word_list = ["john beecher", "patrick brown", "charlie coyle", "jake debrusk", "trent frederic", "morgan geekie", "danton heinen", "jakub lauko", "milan lucic", "brad marchand", "david pastrnak", "matthew poitras", "oskar steen", "pavel zacha", "james vanriemsdyk", "brandon carlo", "derek forbort", "matt grzelcyk", "hampus lindholm", "mason lohrei", "charlie mcavoy", "ian mitchell", "kevin shattenkirk", "jeremy swayman", "linus ullmark"]
        return random.choice(word_list)
    
    # same as function outside of the class, but this is self contained. Separates the logic and overall maintainenance of the code
    def display_word(self):
        display = ""
        for letter in self.word:
            if letter == " ":
                display += "  "
            elif letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        self.display.set(display)

    # method for guessing a letter
    def guess_letter(self, event):
        # make guess lowercase
        guess = self.entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        else:
            # clears textbox
            self.entry.delete(0, tk.END)  

            if guess in self.guessed_letters:
                messagebox.showwarning("Already Guessed", "You already guessed that letter.")
            else:
                # add the guess to the guessed letters list
                self.guessed_letters.append(guess)

                if guess not in self.word:
                    # increase the attempts and update the hangman image
                    self.attempts += 1
                    self.canvas.itemconfig(self.image_display, image=self.images[self.attempts])

                # setting the display for the current state of the word being guessed
                self.display.set(display_word(self.word, self.guessed_letters))

                # winning!
                if "_" not in self.display.get():
                    messagebox.showinfo("Congratulations!", "You've guessed the player!")
                    self.play_again_button.pack()
                    self.write_to_file("Win: " + self.word)
                    self.write_to_mongodb("Win")

                # losing
                if self.attempts == self.max_attempts:
                    messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The player was: {self.word}")
                    self.play_again_button.pack()
                    self.write_to_file("Loss: " + self.word)
                    self.write_to_mongodb("Loss")

    # reset the game
    def reset_game(self):
        self.word = self.select_word()
        self.attempts = 0
        self.guessed_letters = []
        self.display.set(display_word(self.word, self.guessed_letters))
        self.canvas.itemconfig(self.image_display, image=self.images[0])
        self.play_again_button.pack_forget()  

# checks if running directly
if __name__ == "__main__":
    # creates main window
    root = tk.Tk()
    # title of the window
    root.title("2023-2024 Boston Bruins Hangman Game")
    # initializes game in the GUI
    game = HangmanGame(root)
    game.read_stats_file()
    # keeps the GUI running
    root.mainloop()
