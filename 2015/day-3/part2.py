#%%
def openInput():
    with open('input.txt') as f:
        return f.read()

class House():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.gifts = 0
    
    def addGift(self):
        self.gifts += 1

class Houses():
    def __init__(self) -> None:
        self.houses: list[House] = []

    def addHouse(self, house: House):
        self.houses.append(house)

    def getHouse(self, x, y) -> bool:
        for house in self.houses:
            if house.x == x and house.y == y:
                return house
        new_house = House(x,y)
        self.houses.append(new_house)
        return new_house

def move(x, y, cmd):
    if cmd == '<':
        x -= 1
    elif cmd == '>':
        x += 1
    elif cmd == '^':
        y += 1
    elif cmd == 'v':
        y -= 1
    return x, y

def isEven(n: int) -> bool:
    return n % 2 == 0

line = openInput()
houses = Houses()

# first house
santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0
house = houses.getHouse(santa_x,santa_y)
house.addGift()

# the rest
for (idx, cmd) in enumerate(line):
    if (isEven(idx)):
        santa_x, santa_y = move(santa_x, santa_y, cmd)
        house = houses.getHouse(santa_x, santa_y)
    else:
        robo_x, robo_y = move(robo_x, robo_y, cmd)
        house = houses.getHouse(robo_x, robo_y)
    house.addGift()
    # print(f'added gift at {x=}, {y=}')

print(len(houses.houses))

# %%
