import tkinter as tk
from tkinter import messagebox

# Initialize the board
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

class ChessGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chess Game")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.selected = None
        self.canvas.bind("<Button-1>", self.click)
        self.root.bind("<Key>", self.key_press)
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.editmenu.add_command(label="Copy", command=self.copy_board)

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(8):
            for j in range(8):
                color = "white" if (i+j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50, fill=color)
                if board[j][i] != " ":
                    self.canvas.create_text(i*50+25, j*50+25, text=board[j][i], font=("Arial", 24))

    def click(self, event):
        x, y = event.x // 50, event.y // 50
        if self.selected is None:
            self.selected = (x, y)
        else:
            self.move_piece((self.selected[0], self.selected[1]), (x, y))
            self.selected = None
        self.draw_board()

    def key_press(self, event):
        if event.keysym == "Up" and self.selected:
            self.move_piece(self.selected, (self.selected[0], self.selected[1]-1))
            self.selected = (self.selected[0], self.selected[1]-1)
        elif event.keysym == "Down" and self.selected:
            self.move_piece(self.selected, (self.selected[0], self.selected[1]+1))
            self.selected = (self.selected[0], self.selected[1]+1)
        elif event.keysym == "Left" and self.selected:
            self.move_piece(self.selected, (self.selected[0]-1, self.selected[1]))
            self.selected = (self.selected[0]-1, self.selected[1])
        elif event.keysym == "Right" and self.selected:
            self.move_piece(self.selected, (self.selected[0]+1, self.selected[1]))
            self.selected = (self.selected[0]+1, self.selected[1])
        self.draw_board()

    def move_piece(self, f, t):
        if 0 <= f[0] < 8 and 0 <= f[1] < 8 and 0 <= t[0] < 8 and 0 <= t[1] < 8:
            board[t[1]][t[0]] = board[f[1]][f[0]]
            board[f[1]][f[0]] = " "

    def copy_board(self):
        board_str = "\n".join([" ".join(row) for row in board])
        self.root.clipboard_clear()
        self.root.clipboard_append(board_str)
        messagebox.showinfo("Copied", "Board copied to clipboard!")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = ChessGame()
    game.run()
