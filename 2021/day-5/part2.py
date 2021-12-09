#%%
import os

class Grid():
    def __init__(self) -> None:
        self.grid = [[0 for j in range(0,1000)] for i in range(0,1000)]

    def addCount(self, coord):
        x, y = coord
        self.grid[x][y] += 1

    def getCountGreaterThanN(self, n: int) -> int:
        total = 0
        for x in self.grid:
            for y in x:
                if y > n:
                    total += 1
        return total

class Line():
    def __init__(self, text: str) -> None:
        parsed_test = [i.split(',') for i in text.split(' -> ')]
        self.x1 = int(parsed_test[0][0])
        self.y1 = int(parsed_test[0][1])
        self.x2 = int(parsed_test[1][0])
        self.y2 = int(parsed_test[1][1])
        self.min_x = min(self.x1, self.x2)
        self.max_x = max(self.x1, self.x2)
        self.min_y = min(self.y1, self.y2)
        self.max_y = max(self.y1, self.y2)

    def isVertical(self):
        return self.x1 == self.x2

    def isHorizontal(self):
        return self.y1 == self.y2

    def isAscendingDiagonal(self):
        # if diff between x1 and x2 is same sign as diff between y1 and y2
        diff_x = self.x1 - self.x2
        diff_y = self.y1 - self.y2
        return (diff_x < 0 and diff_y < 0) or (diff_x > 0 and diff_y > 0)

    def isDescendingDiagonal(self):
        # if diff between x1 and x2 is opposite sign as diff between y1 and y2
        # don't actually need it due to process of elimination
        pass

    def pointsCovered(self):
        if self.isVertical():
            return [(self.x1, i) for i in range(self.min_y, self.max_y+1)]
        elif self.isHorizontal():
            return [(i, self.y1) for i in range(self.min_x, self.max_x+1)]
        elif self.isAscendingDiagonal():
            return [(self.min_x+i, self.min_y+i) for i in range(self.max_y-self.min_y+1)]
        else: # descending diagonal
            return [(self.max_x-i, self.min_y+i) for i in range(self.max_y-self.min_y+1)]

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

raw_lines = openInput()
grid = Grid()
lines = []

for raw_line in raw_lines:
    line = Line(raw_line)
    
    points_covered = line.pointsCovered()
    if points_covered != None:
        for coord in points_covered:
            grid.addCount(coord)

print(f'{grid.getCountGreaterThanN(1)=}')
print('done')