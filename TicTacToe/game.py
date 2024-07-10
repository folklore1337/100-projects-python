# Код с сайта RealPython. Я добавил возможность игры с компьютером и другом. Режим можно выбрать в меню.
# Дополнил выбором сложности игры.

import tkinter as tk
from tkinter import font
import random

class TicTacToeGame:
    def __init__(self):
        self.board_size = 3
        self.reset_game()

    def reset_game(self):
        self.board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = Player("X", "blue")
        self.other_player = Player("O", "green")
        self.winner_combo = []

    def is_valid_move(self, move):
        row, col = move.row, move.col
        return self.board[row][col] is None

    def process_move(self, move):
        self.board[move.row][move.col] = move.label
        if self.check_winner(move):
            self.winner_combo = self.get_winning_combo(move)

    def toggle_player(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def is_tied(self):
        return all(cell is not None for row in self.board for cell in row)

    def has_winner(self):
        return len(self.winner_combo) > 0

    def check_winner(self, move):
        row, col = move.row, move.col
        label = move.label
        board = self.board

        def all_equal(lst):
            return all(x == label for x in lst)

        row_win = all_equal(board[row])
        col_win = all_equal([board[r][col] for r in range(self.board_size)])
        diag1_win = all_equal([board[i][i] for i in range(self.board_size)])
        diag2_win = all_equal([board[i][self.board_size - i - 1] for i in range(self.board_size)])
        return row_win or col_win or diag1_win or diag2_win

    def get_winning_combo(self, move):
        row, col = move.row, move.col
        label = move.label
        board = self.board

        def get_indices(lst):
            return [(i, j) for i, row in enumerate(lst) for j, cell in enumerate(row) if cell == label]

        if all(x == label for x in board[row]):
            return [(row, i) for i in range(self.board_size)]
        if all(x == label for x in [board[r][col] for r in range(self.board_size)]):
            return [(i, col) for i in range(self.board_size)]
        if all(x == label for x in [board[i][i] for i in range(self.board_size)]):
            return [(i, i) for i in range(self.board_size)]
        if all(x == label for x in [board[i][self.board_size - i - 1] for i in range(self.board_size)]):
            return [(i, self.board_size - i - 1) for i in range(self.board_size)]
        return []

class Player:
    def __init__(self, label, color):
        self.label = label
        self.color = color

class Move:
    def __init__(self, row, col, label):
        self.row = row
        self.col = col
        self.label = label

class TicTacToeBoard(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self._game = game
        self._cells = {}
        self.title("Tic-Tac-Toe")
        self._create_menu()
        self._create_display()
        self._create_board_grid()
        self.play_with_computer = False

    def _create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="Play with Computer", command=self._set_computer_mode)
        game_menu.add_command(label="Play with Friend", command=self._set_friend_mode)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.quit)

    def _set_computer_mode(self):
        self.play_with_computer = True
        self.reset_board()

    def _set_friend_mode(self):
        self.play_with_computer = False
        self.reset_board()

    def _create_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack()
        self.display = tk.Label(master=display_frame, text="Ready?", font=font.Font(size=28, weight="bold"))
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=70, weight="bold"),
                    fg="black",
                    width=3,
                    height=1,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def play(self, event):
        """Handle a player's move."""
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            elif self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")
            else:
                self._game.toggle_player()
                if self.play_with_computer and self._game.current_player.label == "O":
                    self._computer_move()
                else:
                    msg = f"{self._game.current_player.label}'s turn"
                    self._update_display(msg)

    def _computer_move(self):
        available_moves = [
            (row, col) for row in range(self._game.board_size)
            for col in range(self._game.board_size) if self._game.board[row][col] is None
        ]
        row, col = random.choice(available_moves)
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            for button, coordinates in self._cells.items():
                if coordinates == (row, col):
                    self._update_button(button)
                    break
            self._game.process_move(move)
            if self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            elif self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        """Reset the game's board to play again."""
        self._game.reset_game()
        self._update_display(msg="Ready?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")

def main():
    """Create the game's board and run its main loop."""
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()

if __name__ == "__main__":
    main()
