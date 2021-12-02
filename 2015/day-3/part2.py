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


line = openInput()
houses = Houses()

# first house
x, y = 0, 0
house = houses.getHouse(x,y)
house.addGift()

# the rest
for cmd in line:
    x, y = move(x, y, cmd)
    house = houses.getHouse(x,y)
    house.addGift()
    # print(f'added gift at {x=}, {y=}')

print(len(houses.houses))

# %%
