import sys
from PIL import Image, ImageDraw, ImageFont

class Sudoku:
    def __init__(self):
        self.board = []

    def build(self):
        with open('boards/board1.txt', 'r') as file:
            column = []
            for char in file.read():
                if char not in ['\n', '|']:
                    column.append(char)

                if char == '\n':
                    self.board.append(column)
                    column = []
            else:
                self.board.append(column)

    def visualize(self):
        bs = 75
        dimension = ((len(self.board[0])) * bs + 1, (len(self.board)) * bs + 1)

        img = Image.new('RGB', dimension)
        drw = ImageDraw.Draw(img)

        for rk, rv in enumerate(self.board):
            gr = 2 if rk % 3 == 0 and rk != 0 else 0
            for ck, cv in enumerate(rv):
                gc = 2 if ck % 3 == 0 and ck != 0 else 0
                tile = (234, 231, 230) if cv != ' ' else (255, 255, 255)
                font = ImageFont.truetype('assets/Lato-Bold.ttf', 25)

                pos = [(ck * bs) + gc, (rk * bs) + gr, (ck + 1) * bs, (rk + 1) * bs]
                drw.rectangle(pos, tile, outline=(0, 0, 0), width=1)
                drw.text(((ck * bs) + 30, (rk * bs) + 20), cv, font=font, fill=(0, 0, 0))

        img.show()

if __name__ == '__main__':
    sudoku = Sudoku()
    sudoku.build()
    sudoku.visualize()