import os

class Fish():
    def __init__(self, age) -> None:
        self.age = age

    def incrementAge(self):
        self.age = self.age-1 if self.age > 0 else 6

    def produceBaby(self):
        return self.age == 0

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return [Fish(int(i)) for i in f.read().split(',')]

num_days = 80
fishes = openInput()

for day in range(1,num_days+1):
    new_fish_count = 0
    for fish in fishes:
        if fish.produceBaby():
            new_fish_count += 1
        fish.incrementAge()
    fishes += [Fish(8) for i in range(0, new_fish_count)]
    print(len(fishes))



