#%%
import os

class Cell():
    def __init__(self, value) -> None:
        self.value = value
        self.matched = False

    def markMatched(self) -> None:
        self.matched = True

class Card():
    def __init__(self, lines) -> None:
        self.raw_grid = [line.split() for line in lines] # 5x5 2d array
        self.grid = [['' for j in range(0,5)] for i in range(0,5)]
        self.total = 0
        self.done = False
        for (y, row) in enumerate(self.raw_grid):
            for (x, value) in enumerate(row):
                int_value = int(value)
                self.total += int_value
                self.setCell(x, y, int_value)

    def setCell(self, x, y, value):
        self.grid[y][x] = Cell(value)

    def isWinner(self) -> bool:
        return self.checkRows() or self.checkCols()

    def checkRows(self) -> bool:
        for row_num in range(0,5):
            if checkCellsList(self.getRow(row_num)):
                return True
        return False

    def checkCols(self) -> bool:
        for col_num in range(0,5):
            if checkCellsList(self.getCol(col_num)):
                return True
        return False

    def getRow(self, y) -> list[Cell]:
        return self.grid[y]

    def getCol(self, x) -> list[Cell]:
        return [i[x] for i in self.grid]

    def findMatch(self, value):
        for y in self.grid:
            for cell in y:
                if cell.value == value:
                    cell.markMatched()

    def getSumOfUnmatched(self) -> int:
        total = 0
        for y in self.grid:
            for cell in y:
                if not cell.matched:
                    total += cell.value
        return total


def checkCellsList(cells: list[Cell]):
    for cell in cells:
        if not cell.matched:
            return False
    return True

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()


#%%
cards_start_at_line = 2
card_size = 5
cards: list[Card] = []

# create array for Card objects
lines = openInput()
for row in range(cards_start_at_line,len(lines),card_size+1):
    cards.append(Card(lines[row:row+card_size]))
total_cards = len(cards)
done_cards = 0

# draw numbers and keep marking off cards
drawn_nums = lines[0].split(',')
for num in drawn_nums:
    for card in cards:
        # skip ones that are already winners
        if card.done:
            continue

        # otherwise carry on
        card.findMatch(int(num))
        if card.isWinner():
            card.done = True
            done_cards += 1

            # if we're down to 1 non-winner left, we're done
            if done_cards == total_cards:
                print(card.getSumOfUnmatched() * int(num))
                exit()
