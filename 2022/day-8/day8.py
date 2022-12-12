import os


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def main():
    data = openInput()
    grid = [[int(cell) for cell in row.strip()] for row in data]

    # part 1
    part1Answer = getVisibleTreeCount(grid)
    print(f'{part1Answer=}')

    # part 2
    part2Answer = getMaxScore(grid)
    print(f'{part2Answer=}')


def getVisibleTreeCount(grid: list[list[int]]) -> int:
    count = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if isTreeVisible(grid, x, y):
                count += 1
    return count


def getMaxScore(grid):
    maxScore = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            score = getViewScore(grid, x, y)
            if score > maxScore:
                maxScore = score
    return maxScore

    


def getViewScore(grid: list[list[int]], x: int, y: int):
    return viewAbove(grid, x, y) * viewBelow(grid, x, y) * viewLeft(grid, x, y) * viewRight(grid, x, y)


def isTreeVisible(grid: list[list[int]], x: int, y: int) -> bool:
    gridWidth = len(grid[0])
    gridHeight = len(grid)

    # edges are always visible
    if x == 0 or y == 0 or x == gridWidth-1 or y == gridHeight-1:
        return True

    # if any direction is visible, true
    return checkLeft(grid, x, y) or checkRight(grid, x, y) or checkAbove(grid, x, y) or checkBelow(grid, x, y)


def checkLeft(grid: list[list[int]], x: int, y: int):
    targetTree = grid[y][x]
    for i in range(x-1, -1, -1):
        if grid[y][i] >= targetTree:
            return False

    return True


def checkRight(grid: list[list[int]], x: int, y: int):
    targetTree = grid[y][x]
    gridWidth = len(grid[0])
    for i in range(x+1, gridWidth):
        if grid[y][i] >= targetTree:
            return False
    return True


def checkAbove(grid: list[list[int]], x: int, y: int):
    targetTree = grid[y][x]
    for i in range(y-1, -1, -1):
        if grid[i][x] >= targetTree:
            return False
    return True


def checkBelow(grid: list[list[int]], x: int, y: int):
    targetTree = grid[y][x]
    gridHeight = len(grid)
    for i in range(y+1, gridHeight):
        if grid[i][x] >= targetTree:
            return False
    return True


def viewAbove(grid: list[list[int]], x: int, y: int):
    targetTree = grid[y][x]
    treeCount = 0
    for i in range(y-1, -1, -1):
        treeCount += 1
        if grid[i][x] >= targetTree:
            break
    return treeCount


def viewBelow(grid: list[list[int]], x: int, y: int):
    targetTree = grid[y][x]
    gridHeight = len(grid)
    treeCount = 0
    for i in range(y+1, gridHeight):
        treeCount += 1
        if grid[i][x] >= targetTree:
            break
    return treeCount


def viewLeft(grid: list[list[int]], x: int, y: int):
    targetTree = grid[y][x]
    treeCount = 0
    for i in range(x-1, -1, -1):
        treeCount += 1
        if grid[y][i] >= targetTree:
            break
    return treeCount


def viewRight(grid: list[list[int]], x: int, y: int):
    targetTree = grid[y][x]
    gridWidth = len(grid)
    treeCount = 0
    for i in range(x+1, gridWidth):
        treeCount += 1
        if grid[y][i] >= targetTree:
            break
    return treeCount


if __name__ == '__main__':
    main()
