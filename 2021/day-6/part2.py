import os

class FishGroup():
    def __init__(self, age) -> None:
        self.count = 0
        self.age = age

    def incrementAge(self) -> None:
        self.age = self.age-1 if self.age > 0 else 6

    def babiesProduced(self) -> int:
        return self.count if self.age == 0 else 0

    def addFish(self, num) -> None:
        self.count += num

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return [int(i) for i in f.read().split(',')]

def findGroup(fish_groups: list[FishGroup], fish: int):
    for fish_group in fish_groups:
        if fish_group.age == fish:
            fish_group.addFish(1)

def addNewFishToGroup(fish_groups: list[FishGroup], num: int):
    for fish_group in fish_groups:
        if fish_group.age == 8:
            fish_group.addFish(num)

num_days = 256
og_fishes = openInput()

# set up groups
fish_groups: list[FishGroup] = []
for age in range(0,300):
    fish_groups.append(FishGroup(age))

# group og fishes
for fish in og_fishes:
    findGroup(fish_groups, fish)

for day in range(1,num_days+1):
    total = 0
    new_babies = 0
    
    for group in fish_groups:
        new_babies += group.babiesProduced()
        group.incrementAge()
        total += group.count
    
    addNewFishToGroup(fish_groups, new_babies)
    total += new_babies
    
    print(f'Day {day}: {total}')



