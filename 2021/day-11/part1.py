#%%
import os

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

class Point():
    def __init__(self, value) -> None:
        self.value = value
        self.already_flashed = False

    def increaseValue(self) -> None:
        self.value = min(self.value+1, 10)

    def reset(self) -> None:
        if self.value == 10:
            self.value = 0
        self.already_flashed = False

    def flash(self) -> bool:
        if not self.already_flashed:
            self.already_flashed = True
            return True
        return False

class Grid():
    def __init__(self, data: list[str]) -> None:
        self.grid = [[Point(int(x)) for x in y] for y in data]
        self.height = len(data)
        self.width = len(data[0])

    def display(self):
        print('----------')
        for y in self.grid:
            for x in y:
                print(x.value, end='')
            print()
        print()

    def increaseAllPoints(self) -> None:
        for y in self.grid:
            for x in y:
                x.increaseValue()

    def flashTens(self) -> int:
        flashes = 0
        for (y, row) in enumerate(self.grid):
            for (x, point) in enumerate(row):
                if point.value >= 10:
                    if point.flash():
                        flashes += 1
                        self.increaseNeighours(x, y)
        return flashes
    
    def increaseNeighours(self, x, y):
        # probably some easier way to do this :/
        # up
        if y > 0:
            self.grid[y-1][x].increaseValue()

            # up-left
            if x > 0:
                self.grid[y-1][x-1].increaseValue()

            # up-right
            if x < self.width -1:
                self.grid[y-1][x+1].increaseValue()

        # down
        if y < self.height-1:
            self.grid[y+1][x].increaseValue()

            # down-left
            if x > 0:
                self.grid[y+1][x-1].increaseValue()

            # down-right
            if x < self.width -1:
                self.grid[y+1][x+1].increaseValue()

        # left
        if x > 0:
            self.grid[y][x-1].increaseValue()

        # right
        if x < self.width -1:
            self.grid[y][x+1].increaseValue()

    def reset(self) -> int:
        for y in self.grid:
            for x in y:
                x.reset()

    
grid = Grid(openInput())

total_flashes = 0
for step in range(0,100):
    print(f'Step {step}')
    
    # increase energy by 1
    grid.increaseAllPoints()

    cont = True
    while cont:
        result = grid.flashTens()
        if result > 0:
            total_flashes += result
        else:
            cont = False

    grid.display()
    grid.reset()
print(f'{total_flashes=}')


# %%


# %%
