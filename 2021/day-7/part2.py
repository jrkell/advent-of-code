#%%
import os

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return [int(i) for i in f.read().split(',')]

crabs = openInput()

#%%
def getFuelTo(a: int, b: int) -> int:
    start = min(a,b)
    end = max(a,b)
    return sum([i-start for i in range(start, end+1)])

best_spot = {
    "location": -1,
    "fuel": 0
}

for location in range(min(crabs), max(crabs)+1):
    print(f'checking {location=}')
    total_fuel = 0
    for crab in crabs:
        total_fuel += getFuelTo(crab, location)

    if (best_spot["location"] == -1 or total_fuel < best_spot["fuel"]):
        best_spot["location"] = location
        best_spot["fuel"] = total_fuel


print(f'{best_spot["fuel"]=}')