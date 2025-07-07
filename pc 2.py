import tkinter as tk
import random
from tkinter import messagebox

easy_words = ["apple", "mango", "cherry", "banana", "guava"]
medium_words = ["pineapple", "blueberry", "avocado", "strawberry", "kiwifruit"]
hard_words = ["pomegranate", "dragonfruit", "blackcurrant", "watermelon"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🍍 Fruit Hangman")
        self.root.geometry("550x650")
        self.root.configure(bg="#fff0f5")

        self.mode = tk.StringVar(value="Easy")

        # Title
        self.title_label = tk.Label(
            root, text="🍍 Fruit Hangman 🍒",
            font=("Comic Sans MS", 26, "bold"), bg="#fff0f5", fg="#d63384"
        )
        self.title_label.pack(pady=15)

        # Mode Selector
        self.mode_frame = tk.Frame(root, bg="#fff0f5")
        self.mode_frame.pack(pady=5)
        tk.Label(
            self.mode_frame, text="Select Difficulty:",
            font=("Helvetica", 12), bg="#fff0f5"
        ).pack(side=tk.LEFT)
        tk.OptionMenu(
            self.mode_frame, self.mode, "Easy", "Medium", "Hard",
            command=self.restart_game
        ).pack(side=tk.LEFT, padx=10)

        # Word Label
        self.word_label = tk.Label(
            root, text="", font=("Courier", 28), bg="#fff0f5"
        )
        self.word_label.pack(pady=25)

        # Lives
        self.info_label = tk.Label(
            root, text="", font=("Helvetica", 16), bg="#fff0f5", fg="#ff3366"
        )
        self.info_label.pack()

        # Entry
        self.entry = tk.Entry(root, font=("Helvetica", 18), justify='center', width=5)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_guess)

        # Guessed Letters
        self.guessed_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#fff0f5", fg="#555")
        self.guessed_label.pack(pady=10)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="#fff0f5")
        self.button_frame.pack(pady=15)

        self.restart_button = tk.Button(
            self.button_frame, text="🔄 Restart",
            command=self.restart_game,
            font=("Helvetica", 12, "bold"),
            bg="#d63384", fg="white", padx=15, pady=5
        )
        self.restart_button.grid(row=0, column=0, padx=10)

        self.show_button = tk.Button(
            self.button_frame, text="👀 Show Word",
            command=self.show_word,
            font=("Helvetica", 12, "bold"),
            bg="#33b5e5", fg="white", padx=15, pady=5
        )
        self.show_button.grid(row=0, column=1, padx=10)

        self.hint_button = tk.Button(
            self.button_frame, text="💡 Hint",
            command=self.show_hint,
            font=("Helvetica", 12, "bold"),
            bg="#00c851", fg="white", padx=15, pady=5
        )
        self.hint_button.grid(row=0, column=2, padx=10)

        self.celebration_frame = tk.Frame(root, bg="#fff9c4")
        self.celebration_label = tk.Label(
            self.celebration_frame, text="🎉 You Won!", font=("Comic Sans MS", 22, "bold"),
            bg="#fff9c4", fg="#ff6f00"
        )
        self.celebration_label.pack(pady=20)
        self.play_again_button = tk.Button(
            self.celebration_frame, text="🎮 Play Again 🎮",
            font=("Helvetica", 14, "bold"),
            bg="#ff6f00", fg="white",
            command=self.restart_game
        )
        self.play_again_button.pack(pady=10)

        self.restart_game()

    def select_word(self):
        mode = self.mode.get()
        if mode == "Easy":
            self.lives = 8
            return random.choice(easy_words)
        elif mode == "Medium":
            self.lives = 6
            return random.choice(medium_words)
        else:
            self.lives = 4
            return random.choice(hard_words)

    def restart_game(self, *args):
        self.word = self.select_word()
        self.guessed = []
        self.entry.config(state='normal')
        self.word_label.config(text=self.display_word())
        self.info_label.config(text=f"Lives: {self.lives} 💚")
        self.guessed_label.config(text="")
        self.entry.delete(0, tk.END)
        self.celebration_frame.pack_forget()

    def display_word(self):
        return " ".join([letter if letter in self.guessed else "_" for letter in self.word])

    def check_guess(self, event):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        if not letter or not letter.isalpha() or len(letter) != 1:
            messagebox.showwarning("Invalid Input", "Enter a single letter.")
            return
        if letter in self.guessed:
            messagebox.showinfo("Already Guessed", f"You already guessed '{letter}'.")
            return
        self.guessed.append(letter)
        if letter not in self.word:
            self.lives -= 1
        self.word_label.config(text=self.display_word())
        self.info_label.config(text=f"Lives: {self.lives} 💚")
        self.guessed_label.config(text=f"Guessed: {' '.join(self.guessed)}")
        if "_" not in self.display_word():
            self.show_celebration()
        elif self.lives == 0:
            messagebox.showerror("💀 Game Over", f"You lost! The word was: {self.word}")
            self.disable_game()

    def show_celebration(self):
        self.disable_game()
        self.celebration_frame.pack(pady=30)

    def disable_game(self):
        self.entry.config(state='disabled')

    def show_word(self):
        messagebox.showinfo("Word Reveal", f"The word is: {self.word}")

    def show_hint(self):
        hint = self.word[0]
        messagebox.showinfo("Hint", f"The word starts with '{hint}'.")
        if hint not in self.guessed:
            self.guessed.append(hint)
            self.word_label.config(text=self.display_word())

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
