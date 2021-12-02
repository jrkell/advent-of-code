#%%
def openInput():
    with open('input.txt') as f:
        return f.read().splitlines()

class Present():
    def __init__(self, l, w, h) -> None:
        self.l = l
        self.w = w
        self.h = h
    
    def getArea(self) -> int:
        first = self.l * self.w
        second = self.w * self.h
        third = self.h * self.l
        return 2*first + 2*second + 2*third + min(first, second, third)

lines = openInput()

totalArea = 0
for line in lines:
    split = [int(x) for x in line.split('x')]
    present = Present(split[0], split[1], split[2])
    totalArea += present.getArea()

print(f'{totalArea=}')
# %%
