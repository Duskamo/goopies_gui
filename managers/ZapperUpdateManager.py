
import random
import math

class ZapperUpdateManager:
    def __init__(self,zapper):
        self.zapper = zapper

    def zapperMoveRandom(self):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        self.zapper.move(x * self.zapper.speed, y * self.zapper.speed)

    def zapperMoveNearestGoopie(self):
        # 1. sort goopies by closest first
        closestGoopies = []
        for i in range(len(self.zapper.goopies)):
            distance = math.sqrt((self.zapper.goopies[i].x - self.zapper.x) ** 2 + (self.zapper.goopies[i].y - self.zapper.y) ** 2)
            closestGoopies.append({'goopie': self.zapper.goopies[i], 'distance': distance})
        closestGoopies.sort(key=lambda x: x['distance'])

        # 2. travel to goopie
        if self.zapper.x < closestGoopies[0]['goopie'].x and self.zapper.y < closestGoopies[0]['goopie'].y:  # Move SE
            self.zapper.move(1 * self.zapper.speed, 1 * self.zapper.speed)
        elif self.zapper.x == closestGoopies[0]['goopie'].x and self.zapper.y < closestGoopies[0]['goopie'].y:  # Move S
            self.zapper.move(0 * self.zapper.speed, 1 * self.zapper.speed)
        elif self.zapper.x > closestGoopies[0]['goopie'].x and self.zapper.y < closestGoopies[0]['goopie'].y:  # Move SW
            self.zapper.move(-1 * self.zapper.speed, 1 * self.zapper.speed)
        elif self.zapper.x > closestGoopies[0]['goopie'].x and self.zapper.y == closestGoopies[0]['goopie'].y:  # Move W
            self.zapper.move(-1 * self.zapper.speed, 0 * self.zapper.speed)
        elif self.zapper.x > closestGoopies[0]['goopie'].x and self.zapper.y > closestGoopies[0]['goopie'].y:  # Move NW
            self.zapper.move(-1 * self.zapper.speed, -1 * self.zapper.speed)
        elif self.zapper.x == closestGoopies[0]['goopie'].x and self.zapper.y > closestGoopies[0]['goopie'].y:  # Move N
            self.zapper.move(0 * self.zapper.speed, -1 * self.zapper.speed)
        elif self.zapper.x < closestGoopies[0]['goopie'].x and self.zapper.y > closestGoopies[0]['goopie'].y:  # Move NE
            self.zapper.move(1 * self.zapper.speed, -1 * self.zapper.speed)
        elif self.zapper.x < closestGoopies[0]['goopie'].x and self.zapper.y == closestGoopies[0]['goopie'].y:  # Move E
            self.zapper.move(1 * self.zapper.speed, 0 * self.zapper.speed)