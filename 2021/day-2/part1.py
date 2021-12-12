class Position():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def up(self, amount) -> None:
        self.y -= amount

    def down(self, amount) -> None:
        self.y += amount
    
    def forward(self, amount) -> None:
        self.x += amount

def openInput():
    with open('input1.txt') as f:
        return f.read().splitlines()

def doInstruction(line, position: Position) -> None:
    arr = line.split(' ')
    direction = arr[0]
    amount = int(arr[1])
    if direction == 'up':
        position.up(amount)
    if direction == 'down':
        position.down(amount)
    if direction == 'forward':
        position.forward(amount)

lines = openInput()
position = Position()
for line in lines:
    doInstruction(line, position)

x = position.x
y = position.y

print(f'{x=} and {y=} and their product is {x*y}')