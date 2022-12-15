import os
import time

GRID_X_START = 300
GRID_X_END = 700
GRID_HEIGHT = 200
ENTRY_POINT = (500, 0)

AIR = '.'
ROCK = '#'
SAND = '+'
REST = 'o'


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def main(part: int):
    data = openInput()

    grid = {}
    for x in range(GRID_X_START, GRID_X_END):
        for y in range(0, GRID_HEIGHT):
            grid[(x, y)] = AIR
    grid[ENTRY_POINT] = SAND

    rocks = getRocks(data)
    highestY = addRocks(rocks, grid)

    if part == 2:
        addFloor(grid, highestY)

    count = calculateSand(grid)
    # count = animateSand(grid)

    if part == 2:
        count += 1  # to include the entry point

    return count


def addFloor(grid: dict, highestY: int) -> None:
    addRock((GRID_X_START, highestY+2), (GRID_X_END-1, highestY+2), grid)


def animateSand(grid):
    SLEEP = 0.01
    count = 0
    while dropSand(grid):
        printGrid(grid)
        time.sleep(SLEEP)
        count += 1
        os.system('cls')
    return count


def calculateSand(grid):
    # same as animateSand without any animation
    count = 0
    while dropSand(grid):
        count += 1
    return count


def dropSand(grid: dict) -> bool:
    currentX, currentY = ENTRY_POINT
    while True:
        if currentY >= GRID_HEIGHT-1:
            # oh no my sand has fallen into the abyss!!
            return False

        # move down if free
        if grid[(currentX, currentY+1)] == AIR:
            currentY += 1
            continue

        # else move down-left
        if grid[(currentX-1, currentY+1)] == AIR:
            currentY += 1
            currentX -= 1
            continue

        # else move down-right
        if grid[(currentX+1, currentY+1)] == AIR:
            currentY += 1
            currentX += 1
            continue

        # else rest
        grid[(currentX, currentY)] = REST

        # end for part 2
        if (currentX, currentY) == ENTRY_POINT:
            return False

        # else carry on
        return True


def getRocks(data: list[str]) -> list[tuple[int, int]]:
    rocks = []
    for line in data:
        rock = []
        splitLine = line.split(' -> ')
        for point in splitLine:
            rock.append(tuple([int(i) for i in point.strip().split(',')]))
        rocks.append(rock)
    return rocks


def addRocks(rocks: list[tuple[int, int]], grid: dict) -> int:
    highestY = 0
    for rock in rocks:
        for index in range(0, len(rock)-1):
            startPoint = rock[index]
            endPoint = rock[index+1]
            y = addRock(startPoint, endPoint, grid)
            if y > highestY:
                highestY = y
    return highestY


def addRock(startPoint: tuple[int, int], endPoint: tuple[int, int], grid: dict) -> int:
    highestY = 0
    startX, startY = startPoint
    endX, endY = endPoint

    # vertical line
    if startX == endX:
        minY = min(startY, endY)
        maxY = max(startY, endY)
        for y in range(minY, maxY+1):
            grid[(startX, y)] = ROCK
            if y > highestY:
                highestY = y

    # horizontal line
    if startY == endY:
        minX = min(startX, endX)
        maxX = max(startX, endX)
        for x in range(minX, maxX+1):
            grid[(x, startY)] = ROCK

    return highestY


def printGrid(grid: dict) -> None:
    # for y in range(0, GRID_HEIGHT): # too large to see in terminal
    for y in range(0, 75):
        for x in range(GRID_X_START, GRID_X_END):
            print(grid[(x, y)], end='')
        print()


if __name__ == '__main__':
    print("Part 1:", main(1))
    print("Part 2:", main(2))
