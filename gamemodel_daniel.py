# In class Game
def __init__(self, cannonSize, ballSize):
    self.cannonSize = cannonSize
    self.ballSize = ballSize
    self.players = [Player(self, False, -90, "blue"), Player(self, True, 90, "red")]
    self.currentPlayer = 0
    self.wind = random.random() * 20 - 10

def getPlayers(self):
    return self.players

def getCannonSize(self):
    return self.cannonSize

def getBallSize(self):
    return self.ballSize


# In class Player
def __init__(self, game, isReversed, xPos, color):
    self.game = game
    self.isReversed = isReversed
    self.x = xPos
    self.color = color
    self.score = 0
    self.angle = 45
    self.velocity = 40

def getColor(self):
    return self.color

def getX(self):
    return self.x
