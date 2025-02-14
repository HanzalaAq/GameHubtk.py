import tkinter as tk
from tkinter import messagebox
import random
import time
from PIL import Image, ImageTk

# Main Menu
class GameMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Menu")
        self.root.geometry("800x450")
        self.root.configure(bg="#2C3E50")

        self.title_label = tk.Label(
            self.root, 
            text="Welcome to the GameHub!\n Project by Zaid, Shanawar, Rauf and Hanzala", 
            font=("Helvetica", 24, "bold"), 
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        self.title_label.pack(pady=30)

        button_style = {
            "font": ("Arial", 16, "bold"),
            "bg": "#3498DB",
            "fg": "#FFFFFF",
            "activebackground": "#2980B9",
            "activeforeground": "#FFFFFF",
            "width": 20,
            "height": 2,
            "bd": 0,
            "relief": tk.FLAT
        }

        self.hangman_button = tk.Button(
            self.root, 
            text="Play Hangman", 
            command=self.start_hangman,
            **button_style
        )
        self.hangman_button.pack(pady=10)

        self.typing_speed_button = tk.Button(
            self.root, 
            text="Typing Speed Test", 
            command=self.start_typing_speed,
            **button_style
        )
        self.typing_speed_button.pack(pady=10)

        self.rps_button = tk.Button(
            self.root, 
            text="Rock, Paper, Scissors", 
            command=self.start_rps,
            **button_style
        )
        self.rps_button.pack(pady=10)

    def start_hangman(self):
        self.root.withdraw()
        game_window = tk.Toplevel(self.root)
        hangman_game = HangmanGame(game_window)
        game_window.protocol("WM_DELETE_WINDOW", lambda: self.on_game_close(game_window))

    def start_typing_speed(self):
        self.root.withdraw()
        game_window = tk.Toplevel(self.root)
        typing_speed_game = TypingSpeedTestApp(game_window)
        game_window.protocol("WM_DELETE_WINDOW", lambda: self.on_game_close(game_window))

    def start_rps(self):
        self.root.withdraw()
        game_window = tk.Toplevel(self.root)
        rps_game = MyWindow(game_window)
        game_window.protocol("WM_DELETE_WINDOW", lambda: self.on_game_close(game_window))

    def on_game_close(self, game_window):
        game_window.destroy()
        self.root.deiconify()

# Rock, Paper, Scissors Game
class MyWindow:
    def __init__(self, win):
        self.win = win
        self.p = 0  # Player wins
        self.c = 0  # Computer wins
        self.d = 0  # Draws
        self.r = 0  # Rounds

        win.title("Rock, Paper, Scissors")
        win.geometry("800x500")
        win.configure(bg="#F0F0F0")

        self.lb2 = tk.Label(win, text="Player Wins: 0", font=8)
        self.lb2.place(x=60, y=440)

        self.lb3 = tk.Label(win, text="Draws: 0", font=8)
        self.lb3.place(x=350, y=440)

        self.lb4 = tk.Label(win, text="Computer Wins: 0", font=8)
        self.lb4.place(x=580, y=440)

        self.lb5 = tk.Label(win, text='', font=12, bg='#F0F0F0')
        self.lb5.place(x=295, y=280)

        self.lb6 = tk.Label(win, text='', font=12, bg='#F0F0F0')
        self.lb6.place(x=295, y=330)

        self.lb7 = tk.Label(win, text='', font=12, bg='#F0F0F0')
        self.lb7.place(x=295, y=380)

        self.b1 = tk.Button(win, text="Rock", command=lambda: self.rps('Rock'), padx=14, pady=7, bg='red', font=14)
        self.b1.place(x=145, y=120)

        self.b2 = tk.Button(win, text="Paper", command=lambda: self.rps('Paper'), padx=12, pady=7, bg='yellow', font=14)
        self.b2.place(x=295, y=120)

        self.b3 = tk.Button(win, text="Scissors", command=lambda: self.rps('Scissors'), padx=8, pady=7, bg='#09B537', font=14)
        self.b3.place(x=445, y=120)

    def rps(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        self.r += 1
        result = ""

        if player_choice == computer_choice:
            result = "It's a tie!"
            self.d += 1
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win the round!"
            self.p += 1
        else:
            result = "You lose the round!"
            self.c += 1

        self.update_scores()

        self.lb5.config(text=f"Your choice: {player_choice}")
        self.lb6.config(text=f"Computer's choice: {computer_choice}")
        self.lb7.config(text=f"Round Result: {result}")

        if self.r == 5:  # Game ends after 5 rounds
            self.show_final_result()

    def update_scores(self):
        self.lb2.config(text=f"Player Wins: {self.p}")
        self.lb3.config(text=f"Draws: {self.d}")
        self.lb4.config(text=f"Computer Wins: {self.c}")

    def show_final_result(self):
        if self.p > self.c:
            final_result = "Congratulations! You won the game."
        elif self.c > self.p:
            final_result = "Better luck next time! Computer won the game."
        else:
            final_result = "The game is a draw."

        messagebox.showinfo("Game Over", final_result)
        self.reset_game()

    def reset_game(self):
        self.p = 0
        self.c = 0
        self.d = 0
        self.r = 0
        self.update_scores()
        self.lb5.config(text="")
        self.lb6.config(text="")
        self.lb7.config(text="")

class HangmanGame:
    def _init_(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("404x316")
        self.level = ""
        self.word = ""
        self.to_guess = []
        self.attempts = 6
        self.guessed_letters = set()

        self.image_path = ImageTk.PhotoImage(Image.open(r"C:\Users\Hanzala\OneDrive\Desktop\New folder (6)\hangman bg image (1).png"))
        self.bg_label = tk.Label(self.root, image=self.image_path)
        self.bg_label.place(relwidth=1, relheight=1)

        self.setup_gui()

    def setup_gui(self):
        self.title_label = tk.Label(self.root, text="Welcome to Hangman!", font=("Times New Roman", 24, "bold"),bg='#994C00')
        self.title_label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="START GAME", font=("Arial", 16, "italic","bold"),bg='#808080',command=self.start_game_button_pressed)
        self.start_button.pack(pady=10)

    def start_game_button_pressed(self):
        self.start_button.pack_forget()

        self.level_label = tk.Label(self.root, text="Choose the level:", font=("Arial", 15,"italic","bold"),bg="#000000",fg="#FFFFFF")
        self.level_label.pack(pady=5)

        self.level_button_1 = tk.Button(self.root, text="Easy",font=("Arial", 12,"bold"),bg="#009900",height=2,width=10,command=lambda: self.set_level("1"))
        self.level_button_1.pack(pady=5)

        self.level_button_2 = tk.Button(self.root, text="Intermediate",font=("Arial", 12,"bold"),bg="#CCCC00",height=2,width=10, command=lambda: self.set_level("2"))
        self.level_button_2.pack(pady=7)

        self.level_button_3 = tk.Button(self.root, text="Hard",font=("Arial", 12,"bold"),bg="#CC0000",height=2,width=10, command=lambda: self.set_level("3"))
        self.level_button_3.pack(pady=9)

    def set_level(self, level):
        self.level = level
        if level == "1":
            self.words = ["hangman", "white", "reading", "cars", "tiger", "horse", "animal", "chair", "water", "pen",
                          "phone", "table", "apple", "sugar", "bread", "toe", "pakistan", "india", "china"]
        elif level == "2":
            self.words = ["kangaroo", "frozen", "charcoal", "maroon", "avatar", "avengers", "spark", "wrath", "desire",
                          "deprived", "privileged", "wasp", "charity", "delight", "variable", "dictionary",
                          "algorithms", "string", "delusional"]
        elif level == "3":
            self.words = ["lavender", "turquoise", "magenta", "inception", "interstellar", "gladiator", "nostalgia",
                          "dilemma", "obscure", "stumble", "scribble", "wolverine", "flamingo"]
        else:
            messagebox.showerror("Invalid Level", "Please choose a valid level.")
            return

        self.start_game()

    def start_game(self):
        self.word = random.choice(self.words)
        self.to_guess = ["_"] * len(self.word)
        self.attempts = 6
        self.guessed_letters = set()

        self.update_game_status("You have 6 wrong attempts, Think Carefully!")
        self.update_word_display()

        self.level_label.pack_forget()
        self.level_button_1.pack_forget()
        self.level_button_2.pack_forget()
        self.level_button_3.pack_forget()

        self.guess_label = tk.Label(self.root, text="Enter a letter:", font=("Impact", 12),bg="#FFFF66")
        self.guess_label.pack(pady=5)

        self.guess_entry = tk.Entry(self.root, font=("Arial", 14))
        self.guess_entry.pack(pady=5)

        self.guess_button = tk.Button(self.root, text="Guess",bg="#66FFFF", command=self.make_guess)
        self.guess_button.pack(pady=10)

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            self.update_game_status("Invalid input, Enter a single letter!")
            return

        if guess in self.guessed_letters:
            self.update_game_status("You already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            self.update_game_status(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.to_guess[i] = guess
            self.update_word_display()
        else:
            self.attempts -= 1
            self.update_game_status(
                f"Wrong guess! '{guess}' is not in the word. You have {self.attempts} attempts left.")
            if self.attempts == 0:
                self.end_game(False)

        if "_" not in self.to_guess:
            self.end_game(True)

    def update_word_display(self):
        word_display = " ".join(self.to_guess)
        if hasattr(self, 'word_display_label'):
            self.word_display_label.config(text=word_display)
        else:
            self.word_display_label = tk.Label(self.root, text=word_display, font=("Arial", 14))
            self.word_display_label.pack(pady=10)

    def update_game_status(self, message):
        if hasattr(self, 'status_label'):
            self.status_label.config(text=message)
        else:
            self.status_label = tk.Label(self.root, text=message, font=("Arial", 12))
            self.status_label.pack(pady=5)

    def end_game(self, win):
        if win:
            messagebox.showinfo("Congratulations!", f"You guessed the word '{self.word}'!")
        else:
            messagebox.showinfo("Game Over", f"GAME OVER! The word was '{self.word}'.")

        self.reset_game()

    def reset_game(self):
        self.word_display_label.pack_forget()
        self.guess_entry.delete(0, tk.END)
        self.update_game_status("Click Start Game to play again!")

        self.start_button.pack(pady=10)

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.configure(bg='#8C9A9E')
        self.WORDS = {
            "easy": ["cat", "dog", "book", "pen", "tree","Hello","Good","boy"],
            "medium": ["python", "window", "typing", "speed", "keyboard"],
            "hard": ["accuracy", "challenge", "interface", "programming", "practice"]
        }

      
        self.current_word = ""
        self.start_time = None
        self.typed_words = []
        self.correct_words = 0
        self.difficulty = "easy"  

        # Build GUI
        self.create_widgets()

    def create_widgets(self):
        
        self.instruction_label = tk.Label(
            self.root, text="Type the word displayed below as fast as you can!", font=("Helvetica", 16)
        )
        self.instruction_label.pack(pady=10)

       
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24, "bold"), fg="blue")
        self.word_label.pack(pady=20)

        
        self.entry = tk.Entry(self.root, font=("Helvetica", 16), bd=2, relief="solid")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)

        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), fg="green")
        self.result_label.pack(pady=10)

        
        self.difficulty_frame = tk.Frame(self.root)
        self.difficulty_frame.pack(pady=10)

        self.easy_button = tk.Button(
            self.difficulty_frame, text="Easy", font=("Helvetica", 14), bg="lightgreen",
            command=lambda: self.set_difficulty("easy")
        )
        self.easy_button.grid(row=0, column=0, padx=5)

        self.medium_button = tk.Button(
            self.difficulty_frame, text="Medium", font=("Helvetica", 14), bg="lightblue",
            command=lambda: self.set_difficulty("medium")
        )
        self.medium_button.grid(row=0, column=1, padx=5)

        self.hard_button = tk.Button(
            self.difficulty_frame, text="Hard", font=("Helvetica", 14), bg="lightcoral",
            command=lambda: self.set_difficulty("hard")
        )
        self.hard_button.grid(row=0, column=2, padx=5)

        self.difficulty_label = tk.Label(self.root, text="Difficulty: Easy", font=("Helvetica", 14), fg="purple")
        self.difficulty_label.pack(pady=5)

        self.start_button = tk.Button(
            self.root, text="Start", font=("Helvetica", 16), bg="orange", command=self.start_game
        )
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(
            self.root, text="Reset", font=("Helvetica", 16), bg="red", command=self.reset_game, state=tk.DISABLED
        )
        self.reset_button.pack(pady=10)

    def start_game(self):
        self.start_time = time.time()
        self.correct_words = 0
        self.typed_words = []
        self.start_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)
        self.result_label.config(text="")
        self.display_word()

    def display_word(self):
        self.current_word = random.choice(self.WORDS[self.difficulty])
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def check_word(self, event):
        typed_word = self.entry.get().strip()
        self.typed_words.append(typed_word)

        if typed_word == self.current_word:
            self.correct_words += 1

        if len(self.typed_words) == 10:  
            self.end_game()
        else:
            self.display_word()

    def end_game(self):
        end_time = time.time()
        time_taken = end_time - self.start_time
        words_per_minute = (self.correct_words / time_taken) * 60
        self.result_label.config(
            text=f"Test completed! Words per minute: {words_per_minute:.2f}. Correct words: {self.correct_words}/10"
        )
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
        self.word_label.config(text="")

    def reset_game(self):
        self.start_time = None
        self.correct_words = 0
        self.typed_words = []
        self.result_label.config(text="")
        self.word_label.config(text="")
        self.entry.delete(0, tk.END)
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

    def set_difficulty(self, level):
        self.difficulty = level
        self.difficulty_label.config(text=f"Difficulty: {level.capitalize()}")
        self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameMenu(root)
    root.mainloop()