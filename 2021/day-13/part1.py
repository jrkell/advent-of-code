import os

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

class Point():
    def __init__(self, x, y) -> None:
        self.x = int(x)
        self.y = int(y)

    def foldX(self, fold_x):
        if self.x > fold_x:
            distance_from_hold = self.x - fold_x
            self.x = fold_x - distance_from_hold

    def foldY(self, fold_y):
        if self.y > fold_y:
            distance_from_hold = self.y - fold_y
            self.y = fold_y - distance_from_hold

def createPoints(lines, points):
    for line in lines:
        if line[0:4] != 'fold' and line != '':
            line_split = line.split(',')
            points.append(Point(line_split[0], line_split[1]))

def createFolds(lines, folds):
    for line in lines:
        if line[0:4] == 'fold':
            split_fold = line[11:].split('=')    
            folds.append(split_fold)

def applyFolds(folds, points):
    for fold in folds:
        if fold[0] == 'x':
            for point in points:
                point.foldX(int(fold[1]))
        elif fold[0] == 'y':
            for point in points:
                point.foldY(int(fold[1]))
        break # only care about the first fold here

def removeDuplicatePoints(points):
    used_coords = []
    unique_list = []
    for point in points:
        if (point.x, point.y) in used_coords:
            continue
        else:
            unique_list.append(point)
            used_coords.append((point.x, point.y))

    return unique_list

def main():
    lines = openInput()
    points = []
    folds = []

    createPoints(lines, points)
    createFolds(lines, folds)
    applyFolds(folds, points)
    deduped = removeDuplicatePoints(points)
    print(f'{len(deduped)=}')

if __name__ == '__main__':
    main()