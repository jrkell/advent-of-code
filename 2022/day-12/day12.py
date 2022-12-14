import os
import time

LETTERS = "SabcdefghijklmnopqrstuvwxyzE"


class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.heightNum = LETTERS.find(self.value)

        self.isStart = self.value == 'S'
        self.isEnd = self.value == 'E'

        self.neighbours: list[Node] = []

    def __repr__(self) -> str:
        return self.value

    def canTravelTo(self, neighbour) -> bool:
        return (neighbour.heightNum - self.heightNum) < 2


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def populateNeighbours(grid: list[list[Node]]) -> Node:
    height = len(grid)
    width = len(grid[0])
    for y in range(height):
        for x in range(width):
            node = grid[y][x]
            if node.isStart:
                startNode = node

            # up
            if y > 0:
                node.neighbours.append(grid[y-1][x])

            # down
            if y < height-1:
                node.neighbours.append(grid[y+1][x])

            # left
            if x > 0:
                node.neighbours.append(grid[y][x-1])

            # right
            if x < width-1:
                node.neighbours.append(grid[y][x+1])

    return startNode


def BFS(startNode: Node):
    # https://en.wikipedia.org/wiki/Breadth-first_search
    visited = {}
    visited[startNode] = []
    queue = [startNode]

    while queue:
        current = queue.pop()
        currentSteps = visited[current]

        for neighbour in current.neighbours:
            if neighbour not in visited and current.canTravelTo(neighbour):
                visited[neighbour] = currentSteps + [neighbour]
                queue.insert(0,neighbour)

                if neighbour.isEnd:
                    return visited[neighbour]


def main(part: int):
    data = openInput()
    grid = [[Node(col) for col in row.strip()] for row in data]
    startNode = populateNeighbours(grid)

    if part == 1:
        shortestPath = BFS(startNode)
        animatePath(grid, shortestPath)
        return len(shortestPath)

    if part == 2:
        aNodes = getANodes(grid)
        shortestPaths = [BFS(a) for a in aNodes]
        shortestPathLengths = [len(path) for path in shortestPaths if path != None]
        return min(shortestPathLengths)

def getANodes(grid: list[list[Node]]):
    aNodes = []
    for row in grid:
        for node in row:
            if node.value == 'a':
                aNodes.append(node)
    return aNodes


def animatePath(grid: list[list[Node]], path: list[Node]) -> None:
    alreadyInPath = []
    for node in path:
        os.system('cls')
        for row in grid:
            for cell in row:
                if cell == node:
                    symbol = '#'
                    alreadyInPath.append(cell)
                if cell in alreadyInPath:
                    symbol = '.'
                else:
                    symbol = cell
                print(symbol, end='')
            print('')
        time.sleep(0.05)
        

if __name__ == '__main__':
    print("Part 1 = ", main(1))
    print("Part 2 = ", main(2))
