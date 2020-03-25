
from libs.graphics import *

from models.Corpse import *

class GoopieUpdateManager:
    def __init__(self,goopie):
        self.goopie = goopie

    def updateSkin(self):
        self.goopie.body.undraw()
        self.goopie.body = Circle(Point(self.goopie.x, self.goopie.y), self.goopie.radius)
        self.goopie.body.setWidth(1)
        self.goopie.body.setOutline(self.goopie.color)
        self.goopie.body.draw(self.goopie.win)

    def goopieCorpse(self):
        self.goopie.undraw()
        corpse = Corpse(self.goopie.win, self.goopie.x, self.goopie.y)
        corpse.draw()
        self.goopie = None

    def goopieKeyboardInput(self):
        if self.goopie.keyboardQueue.get() == "Up":
            self.goopie.move(0, -3)
        elif self.goopie.keyboardQueue.get() == "Down":
            self.goopie.move(0, 5)
        elif self.goopie.keyboardQueue.get() == "Left":
            self.goopie.move(-6, 0)
        elif self.goopie.keyboardQueue.get() == "Right":
            self.goopie.move(6, 0)

            self.goopie.keyboardQueue.queue.clear()

    def clearPelletOnContact(self):
        removedPellet = self.goopie.pelletConsumedQueue.get()
        self.goopie.pellets[removedPellet].undraw()
        self.goopie.pellets.pop(removedPellet)