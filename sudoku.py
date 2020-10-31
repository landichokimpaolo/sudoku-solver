import sys
import math
import time

from PIL import Image, ImageDraw, ImageFont

class Sudoku:
    def __init__(self):
        self.board = []
        self.tiles = []
        self.recursion = 0
        sys.setrecursionlimit(10000)

    def build(self):
        with open(sys.argv[1], 'r') as file:
            row = 0
            column = []
            for char in file.read():
                if char not in ['\n', '|']:
                    if int(char) == 0:
                        self.tiles.append((row, len(column)))
                    column.append(int(char))

                if char == '\n':
                    self.board.append(column)
                    column = []
                    row += 1
            else:
                self.board.append(column)

    def visualize(self):
        bs = 75
        dimension = ((len(self.board[0])) * bs + 1, (len(self.board)) * bs + 1)

        img = Image.new('RGB', dimension)
        drw = ImageDraw.Draw(img)
        font = ImageFont.truetype('assets/Lato-Bold.ttf', 25)

        for rk, rv in enumerate(self.board):
            gr = 2 if rk % 3 == 0 and rk != 0 else 0

            for ck, cv in enumerate(rv):
                gc = 2 if ck % 3 == 0 and ck != 0 else 0
                value = str(cv) if cv != 0 else ' '
                position = [(ck * bs) + gc, (rk * bs) + gr, (ck + 1) * bs, (rk + 1) * bs]
                background = (234, 231, 230) if (rk, ck) not in self.tiles else (255, 255, 255)

                drw.rectangle(position, background, outline=(0, 0, 0))
                drw.text(((ck * bs) + 30, (rk * bs) + 20), value, font=font, fill=(0, 0, 0))

        img.show()

    def get_grid(self, row, col):
        rs, cs = (row // 3) * 3, (col // 3) * 3
        re, ce = rs + 3, cs + 3
        tmp = []

        for r in range(rs, re):
            for c in range(cs, ce):
                tmp.append(self.board[r][c])

        return tmp

    def get_next(self, n):
        return n + 1 if n + 1 in range(1, 10) else 10

    def valid(self, n, current):
        row, col = current
        if n not in [self.board[row][n] for n in range(9)]:
            if n not in [self.board[n][col] for n in range(9)]:
                if n not in self.get_grid(row, col):
                    return True
        return False

    def solve(self, t=0, s=1):
        if t < len(self.tiles):
            row, col = self.tiles[t]
            for n in range(s, 10):
                if self.valid(n, (row, col)):
                    self.board[row][col] = n
                    self.solve(t + 1)
                    self.recursion += 1
                    break
            else:
                row, col = self.tiles[t - 1]
                v = self.board[row][col]
                s = self.get_next(v)
                self.board[row][col] = 0
                self.solve(t - 1, s)

if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.build()
    sudoku.solve()
    sudoku.visualize()