#%%
def openInput():
    with open('input.txt') as f:
        return f.read().splitlines()

class Present():
    def __init__(self, l, w, h) -> None:
        self.l = l
        self.w = w
        self.h = h
        self.first_area = l * w
        self.second_area = w * h
        self.third_area = h * l
        self.first_perimeter = 2*l + 2*w
        self.second_perimeter = 2*w + 2*h
        self.third_perimeter = 2*h + 2*l
        self.volume = l * w * h
    
    def getWrappingPaper(self) -> int:
        return 2*self.first_area + 2*self.second_area + 2*self.third_area + min(self.first_area, self.second_area, self.third_area)

    def getRibbon(self) -> int:
        return min(self.first_perimeter, self.second_perimeter, self.third_perimeter) + self.volume
        

lines = openInput()

totalArea = 0
totalRibbon = 0
for line in lines:
    split = [int(x) for x in line.split('x')]
    present = Present(split[0], split[1], split[2])
    totalArea += present.getWrappingPaper()
    totalRibbon += present.getRibbon()

print(f'{totalArea=}')
print(f'{totalRibbon=}')
# %%
