

from math import cos, sin, radians
import random

"""This is the model of the game."""


class Game:
    """Create a game with a given size of cannon and projectile radius."""

    def __init__(self, cannonSize, ballSize):
        self._cannonSize = cannonSize
        self._ballSize = ballSize
        self._players = [
            Player(self, False, -90, "red"),
            Player(self, True, 90, "blue"),
        ]
        self._currentPlayer = 0
        self._currentWind = 0

    def getPlayers(self):
        return self._players

    def getCannonSize(self):
        return self._cannonSize

    def getBallSize(self):
        return self._ballSize

    def getCurrentPlayer(self):
        return self._players[self._currentPlayer]

    def getOtherPlayer(self):
        return self._players[1 - self._currentPlayer]

    def getCurrentPlayerNumber(self):
        return self._currentPlayer

    def nextPlayer(self):
        self._currentPlayer = 1 - self._currentPlayer

    def setCurrentWind(self, wind):
        self._currentWind = wind

    def getCurrentWind(self):
        return self._currentWind

    def newRound(self):
        self._currentWind = random.random() * 20 - 10


class Player:
    """Models a player in the artillery game."""

    def __init__(self, game, IsReversed, x, color):
        self.game = game
        self.IsReversed = IsReversed
        self.x = x
        self.color = color
        self.score = 0
        self.angle = 45
        self.velocity = 40

    def fire(self, angle, velocity):
        self.angle = angle
        self.velocity = velocity

        if self.IsReversed:
            angle = 180 - angle

        wind = self.game.getCurrentWind()
        xpos = self.x
        ypos = self.game.getCannonSize() / 2
        return Projectile(angle, velocity, wind, xpos, ypos, -110, 110)

    def projectileDistance(self, proj):
        halfCannon = self.game.getCannonSize() / 2
        ballRadius = self.game.getBallSize()

        cannonLeft = self.x - halfCannon
        cannonRight = self.x + halfCannon

        ballLeft = proj.getX() - ballRadius
        ballRight = proj.getX() + ballRadius

        if ballRight < cannonLeft:
            return ballRight - cannonRight
        if ballLeft > cannonRight:
            return ballLeft - cannonRight
        return 0

    def getScore(self):
        return self.score

    def increaseScore(self):
        self.score += 1

    def getColor(self):
        return self.color

    def getX(self):
        return self.x

    def getAim(self):
        return self.angle, self.velocity


class Projectile:
    """
    Constructor parameters:
    angle and velocity: the initial angle and velocity of the projectile
        angle 0 means straight east (positive x-direction) and 90 straight up
    wind: The wind speed value affecting this projectile
    xPos and yPos: The initial position of this projectile
    xLower and xUpper: The lowest and highest x-positions allowed
    """

    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        self.wind = wind

    def update(self, time):
        yvel1 = self.yvel - 9.8 * time
        xvel1 = self.xvel + self.wind * time

        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0

        self.yPos = max(self.yPos, 0)

        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)

        self.yvel = yvel1
        self.xvel = xvel1

    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos
