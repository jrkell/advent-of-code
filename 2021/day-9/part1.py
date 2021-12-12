import os

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

class Grid():
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.grid = [['' for j in range(0,width)] for i in range(0,height)]

    def getNeighbours(self, x: int, y: int) -> list[int]:
        neighbours = []

        # up
        if y > 0:
            neighbours.append(self.grid[y-1][x])

        # down
        if y < self.height-1:
            neighbours.append(self.grid[y+1][x])

        # left
        if x > 0:
            neighbours.append(self.grid[y][x-1])

        # right
        if x < self.width -1:
            neighbours.append(self.grid[y][x+1])
        
        return neighbours

def isLowPoint(num: int, neighbours: list[int]) -> bool:
    for value in neighbours:
        if num >= value:
            return False
    return True

lines = openInput()

# populate board
height = len(lines)
width = len(lines[0])
grid = Grid(height, width)
for (y, line) in enumerate(lines):
    for (x, cell) in enumerate(line):
        grid.grid[x][y] = int(cell)

total = 0
count = 0
for y in range(0, height):
    for x in range(0, width):
        value = grid.grid[y][x]
        neighbours = grid.getNeighbours(x, y)
        if isLowPoint(value, neighbours):
            count += 1
            total += value+1
print(f'there are {count=} lowpoints with {total=}')