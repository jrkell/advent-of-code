import os


def openInput() -> list[str]:
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()

class Part1Game:
    def __init__(self, opponent: str, player: str) -> None:
        self.opponent = part1CodeMappings[opponent]
        self.player = part1CodeMappings[player]
        self.shapePoints = shapePoints[self.player]
        self.playerWins = winnerRules[self.player] == self.opponent
        self.isDraw = self.opponent == self.player

    def getPoints(self):
        if self.playerWins:
            return self.shapePoints + 6
        if self.isDraw:
            return self.shapePoints + 3
        
        # else you lost, good day sir
        return self.shapePoints

class Part2Game:
    def __init__(self, opponent: str, result: str) -> None:
        self.opponent = part2CodeMappings[opponent]
        self.result = part2CodeMappings[result]

        self.player = self.getPlayer()
        self.shapePoints = shapePoints[self.player]
        self.playerWins = winnerRules[self.player] == self.opponent
        self.isDraw = self.opponent == self.player

    def getPlayer(self) -> str:
        if self.result == "Draw":
            return self.opponent
        if self.result == "Win":
            return loserRules[self.opponent]
        return winnerRules[self.opponent]

    def getPoints(self):
        if self.playerWins:
            return self.shapePoints + 6
        if self.isDraw:
            return self.shapePoints + 3
        
        # else you lost, good day sir
        return self.shapePoints


winnerRules = {
    "Rock": "Scissors", # left beats right
    "Scissors" : "Paper",
    "Paper": "Rock"
}

loserRules = {
    "Scissors": "Rock",
    "Paper": "Scissors",
    "Rock": "Paper"
}


part1CodeMappings = {
    "A":"Rock",
    "B":"Paper",
    "C":"Scissors",
    "X":"Rock",
    "Y":"Paper",
    "Z":"Scissors",
}

shapePoints = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

part2CodeMappings = {
    "A":"Rock",
    "B":"Paper",
    "C":"Scissors",
    "X":"Lost",
    "Y":"Draw",
    "Z":"Win",
}

def main():
    gamesList = openInput()
    
    # part 1
    games = [Part1Game(row[0], row[2]) for row in gamesList]
    total = sum([game.getPoints() for game in games])
    print(f'Total score is: {total}')

    # part 2
    games = [Part2Game(row[0], row[2]) for row in gamesList]
    total = sum([game.getPoints() for game in games])
    print(f'Total score is: {total}')

if __name__ == '__main__':
    main()

