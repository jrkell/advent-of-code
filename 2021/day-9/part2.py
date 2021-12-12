import os

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

class Point():
    def __init__(self, value) -> None:
        self.value = value
        self.neighbours = []
        self.counted = False

class Grid():
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.grid = [['' for j in range(0,width)] for i in range(0,height)]

    def setNeighbours(self, y: int, x: int):
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
        
        self.grid[y][x].neighbours = neighbours

def isLowPoint(point: Point) -> bool:
    for neighbour in point.neighbours:
        if point.value >= neighbour.value:
            return False
    return True

def getBasin(point: Point) -> int:
    if point.counted or point.value == 9:
        return 0
    point.counted = True
    count = 1
    for neighbour in point.neighbours:
        count += getBasin(neighbour)
    return count

lines = openInput()

# populate board
height = len(lines)
width = len(lines[0])
grid = Grid(height, width)
for (y, line) in enumerate(lines):
    for (x, cell) in enumerate(line):
        grid.grid[y][x] = Point(int(cell))

# populate all the neighbours
for y in range(0, height):
    for x in range(0, width):
        neighbours = grid.setNeighbours(y, x)

# find low points and get their basins
basin_totals = []
for y in range(0, height):
    for x in range(0, width):
        point = grid.grid[y][x]
        if isLowPoint(point):
            print(f'low point at {y=}, {x=}')
            basin_totals.append(getBasin(point))

# calculate answer
basin_totals.sort(reverse=True)
answer = basin_totals[0] * basin_totals[1] * basin_totals[2]
print(f'{answer=}')
