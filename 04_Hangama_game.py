import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry('905x700')
        self.root.title("HANGMAN")
        self.score = 0
        self.run = True
        self.count = 0
        self.win_count = 0
        self.words = ['programming', 'data', 'python', 'code', 'greek', 'computer', 'engineering', 'word', 'science', 'java', 'college', 'player', 'mobile', 'image', 'Machine']
        self.word = random.choice(self.words)
        self.setup_ui()

    def setup_ui(self):
        # Create labels for letters
        self.labels = []
        x = 250
        for i in range(len(self.word)):
            x += 60
            label = tk.Label(self.root, text="_", bg="white", font=("arial", 40))
            label.place(x=x, y=450)
            self.labels.append(label)

        # Create buttons for letters
        self.buttons = []
        for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
            button = tk.Button(self.root, bd=0, command=lambda l=letter: self.check_word(l))
            button.config(bg="red", activebackground="red", font=10, text=letter)
            button.place(x=i * 70, y=595)
            self.buttons.append(button)

        # Exit button
        exit_button = tk.Button(self.root, bd=0, command=self.exit_game)
        exit_button.config(bg="yellow", activebackground="yellow", font=10, text="Exit")
        exit_button.place(x=770, y=10)

        # Score label
        score_label = tk.Label(self.root, text="SCORE: {}".format(self.score), bg="#ffffe7", font=("arial", 25))
        score_label.place(x=10, y=10)

    def check_word(self, letter):
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.win_count += 1
                    self.labels[i].config(text=letter.upper())
            if self.win_count == len(self.word):
                self.score += 1
                self.game_over_message("YOU WON!")
        else:
            self.count += 1
            if self.count == 6:
                self.game_over_message("YOU LOST!")
            else:
                self.update_hangman_image()

    def update_hangman_image(self):
        # Update hangman image
        pass  # Implement this

    def game_over_message(self, message):
        answer = messagebox.askyesno('GAME OVER', f'{message}\nDO WANT TO PLAY AGAIN?')
        if answer:
            self.reset_game()
        else:
            self.root.destroy()

    def reset_game(self):
        self.root.destroy()
        self.__init__(tk.Tk())

    def exit_game(self):
        answer = messagebox.askyesno('ALERT', 'DO YOU WANT TO EXIT THE GAME?')
        if answer:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

