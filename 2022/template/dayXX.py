import os


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def main(part: int):
    pass

if __name__ == '__main__':
    print("Part 1:", main(1))
    print("Part 2:", main(2))
