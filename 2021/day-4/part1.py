def openInput():
    with open('input.txt') as f:
        return f.read().splitlines()

class Card():
    def __init__(self) -> None:
        self.grid = [['' for j in range(0,5)] for i in range(0,5)]

    def setCell(self, x, y, value):
        self.grid[y][x] = value