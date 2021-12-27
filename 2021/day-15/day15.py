import os

unvisited_neighbours_w_distance = []

class Point():
    def __init__(self, value) -> None:
        self.value = value
        self.neighbours: list[Point] = []
        self.isStart = False
        self.isEnd = False
        self.visited = False
        self.distance = 999999999999

def dijkstra(point: Point):
    unvisited_neighbours = [neighbour for neighbour in point.neighbours if not neighbour.visited]

    for neighbour in unvisited_neighbours:
        new_distance = point.distance + neighbour.value
        if neighbour.distance == None or new_distance < neighbour.distance:
            neighbour.distance = new_distance
            unvisited_neighbours_w_distance.append(neighbour)
    
def setNeighbours(points):
    height = len(points)
    width = len(points[0])
    for y, line in enumerate(points):
        for x, _ in enumerate(line):
            point = points[y][x]
            
            if x == 0 and y == 0:
                point.isStart = True
                point.distance = 0
            
            if x == width-1 and y == height-1:
                point.isEnd = True
                
            # up
            if y > 0:
                point.neighbours.append(points[y-1][x])

            # down
            if y < height-1:
                point.neighbours.append(points[y+1][x])

            # left
            if x > 0:
                point.neighbours.append(points[y][x-1])

            # right
            if x < width -1:
                point.neighbours.append(points[y][x+1])

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

def flattenList(the_list):
    return [item for sublist in the_list for item in sublist]    

def wrapNumber(value):
    if value <= 9:
        return value
    return value-9

def expandPoint(value):
    return [[wrapNumber(value+i+j) for i in range(5)] for j in range(5)]

def solve(part2 = False):
    lines = openInput()

    if not part2:
        points = [[Point(int(char)) for char in line] for line in lines]
    if part2:
        expand_amount = 5
        height = len(lines)
        width = len(lines[0])
        points = [[None for x in range(width*expand_amount)] for y in range(height*expand_amount)]
        for y, line in enumerate(lines):
            for x, number in enumerate(line):
                expanded_point = expandPoint(int(number))
                for y_exp, line_exp in enumerate(expanded_point):
                    for x_exp, number_exp in enumerate(line_exp):
                        y_offset = y + (height * y_exp) 
                        x_offset = x + (width * x_exp)
                        points[y_offset][x_offset] = Point(number_exp)

    setNeighbours(points)
    unvisited_points = flattenList(points)[1:]
    dijkstra(points[0][0])

    cont = True
    while cont:
        unvisited_neighbours_w_distance.sort(key=lambda x: x.distance)
        next_point = unvisited_neighbours_w_distance.pop(0)
        unvisited_points.remove(next_point)
        dijkstra(next_point)

        if len(unvisited_points) == 0:
            cont = False

    return points[-1][-1].distance

if __name__ == '__main__':
    print(f'Part 1 = {solve()}')
    print(f'Part 2 = {solve(True)}')