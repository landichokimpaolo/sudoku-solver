import sys
import math
import time

from PIL import Image, ImageDraw, ImageFont

class Sudoku:
    def __init__(self):
        self.board = []
        self.tiles = []
        self.ctr = -1
        self.prev = 0

    def build(self):
        with open('/Users/kim/Sites/python/sudoku/boards/board1.txt', 'r') as file:
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
        font = ImageFont.truetype('/Users/kim/Sites/python/sudoku/assets/Lato-Bold.ttf', 25)

        for rk, rv in enumerate(self.board):
            gr = 2 if rk % 3 == 0 and rk != 0 else 0

            for ck, cv in enumerate(rv):
                gc = 2 if ck % 3 == 0 and ck != 0 else 0
                tile = (234, 231, 230) if cv != 0 else (255, 255, 255)
                value = str(cv) if cv != 0 else ' '
                position = [(ck * bs) + gc, (rk * bs) + gr, (ck + 1) * bs, (rk + 1) * bs]

                drw.rectangle(position, tile, outline=(0, 0, 0))
                drw.text(((ck * bs) + 30, (rk * bs) + 20), value, font=font, fill=(0, 0, 0))

        img.show()

    def get_row(self, row):
        return [self.board[row][n] for n in range(9)]

    def get_col(self, col):
        return [self.board[n][col] for n in range(9)]

    def get_grid(self, row, col):
        rs, cs = math.floor(row / 3) * 3, math.floor(col / 3) * 3
        re, ce = rs + 3, cs + 3
        tmp = []

        for r in range(rs, re):
            for c in range(cs, ce):
                tmp.append(self.board[r][c])

        return tmp

    def get_next(self, n):
        return (n + 1, n + 2) if n + 1 in range(1, 10) else (1, 2)

    def valid(self, n, current):
        row, col = current
        if n not in self.get_row(row):
            if n not in self.get_col(col):
                if n not in self.get_grid(row, col):
                    return True
        return False

    def solve(self, t=0, start=1, end=10):
        row, col = self.tiles[t]

        self.ctr += 1
        self.visualize()
        time.sleep(.4)

        if self.ctr < 5:
            possible = 0
            for n in range(start, end):
                if self.valid(n, (row, col)):
                    possible = n
                    break

            if possible != 0:
                self.board[row][col] = possible
                self.solve(t + 1)
            else:
                t = max(0, t - 1)

                row, col = self.tiles[t]
                value = self.board[row][col]

                if t == 0 and value == 0:
                    self.board[row][col] = start
                    value = start

                start, end = self.get_next(value)
                self.board[row][col] = 0
                self.solve(t, start, end)


if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.build()
    sudoku.solve()