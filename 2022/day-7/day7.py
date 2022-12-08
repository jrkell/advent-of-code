import os
from typing import Self


class Directory:
    def __init__(self, name: str, parent: Self = None) -> None:
        self.name = name
        self.childDirs: list[Directory] = []
        self.parentDir: Directory = parent
        self.fileSizeInDir = 0
        self.totalFileSize = 0

    def getChildDir(self, childName: str) -> Self:
        return [child for child in self.childDirs if child.name == childName][0]


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def main():
    # load data into tree and find the root
    data = openInput()
    node = createDirectoryTree(data)
    root = traverseToRoot(node)

    # part 1
    # traverse through and calculate the totals
    getTotalSize(root)
    
    # find the answer
    totals = getTotalsLessThanOrEqualX(root, 100000)
    part1Answer = sum(totals)
    print(f'{part1Answer=}')

    # part 2
    # calculate minimum space needed
    spaceNeeded = 30000000
    totalDiskSize = 70000000
    freeUp = (totalDiskSize - spaceNeeded - root.totalFileSize) * -1

    # find any node more than that and print the lowest one
    candidateTotals = getTotalsGreaterThanOrEqualX(root, freeUp)
    candidateTotals.sort()
    part2Answer = candidateTotals[0]
    print(f'{part2Answer=}')


def createDirectoryTree(data: list[str]) -> list[Directory]:
    # init
    currentDir = Directory('/')

    for index, row in enumerate(data):
        # skip first row or ls
        if index == 0 or row[0:4] == '$ ls':
            continue

        # add dirs as children
        if row[0:3] == 'dir':
            newDir = Directory(row[4:].strip(), currentDir)
            # directories.append(newDir)
            currentDir.childDirs.append(newDir)
            continue

        # move to child if its cd
        if row[0:4] == '$ cd':
            dirName = row[5:].strip()
            if dirName == '..':
                currentDir = currentDir.parentDir
            else:
                currentDir = currentDir.getChildDir(row[5:].strip())
            continue

        # else it's a file - add the filesize to total
        fileSize = row.split()[0]
        currentDir.fileSizeInDir += int(fileSize)

    return currentDir


def traverseToRoot(directory: Directory) -> Directory:
    while True:
        if directory.parentDir == None:
            return directory

        # else
        directory = directory.parentDir


def getTotalSize(directory: Directory) -> int:
    # add the files in the actual directory
    total = directory.fileSizeInDir
    
    # recursively get totals of the children
    for child in directory.childDirs:
        total += getTotalSize(child)
    
    # populate each node and return total up the chain
    directory.totalFileSize = total
    return total

def getTotalsLessThanOrEqualX(directory: Directory, x: int) -> list[Directory]:
    lessThanX = []

    if directory.totalFileSize <= x:
        lessThanX.append(directory.totalFileSize)

    # recursion again weeeee
    for child in directory.childDirs:
        lessThanX += getTotalsLessThanOrEqualX(child, x)

    return lessThanX


def getTotalsGreaterThanOrEqualX(directory: Directory, x: int) -> list[Directory]:
    greaterThanX = []

    if directory.totalFileSize >= x:
        greaterThanX.append(directory.totalFileSize)

    # one more recursion
    for child in directory.childDirs:
        greaterThanX += getTotalsGreaterThanOrEqualX(child, x)

    return greaterThanX


if __name__ == '__main__':
    main()
