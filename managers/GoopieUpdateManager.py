
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

        self.goopie.thrusterSE.setFill('light grey')
        self.goopie.thrusterSW.setFill('light grey')
        self.goopie.thrusterNE.setFill('light grey')
        self.goopie.thrusterNW.setFill('light grey')

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

    def goopieKeyboardInputFluid(self):
        #print(self.goopie.keyboardQueue.get()['thruster'],self.goopie.keyboardQueue.get()['status'])

        # When thrusters are activated
        if self.goopie.keyboardQueue.get()['thruster'] == ['SW','SE'] and self.goopie.keyboardQueue.get()['status'] == "On":
            self.goopie.thrusterSE.setFill('red')
            self.goopie.thrusterSW.setFill('red')
            self.goopie.move(0, -3)
        elif self.goopie.keyboardQueue.get()['thruster'] == ['NW','NE'] and self.goopie.keyboardQueue.get()['status'] == "On":
            self.goopie.thrusterNE.setFill('red')
            self.goopie.thrusterNW.setFill('red')
            self.goopie.move(0, 5)
        elif self.goopie.keyboardQueue.get()['thruster'] == ['NE'] and self.goopie.keyboardQueue.get()['status'] == "On":
            self.goopie.thrusterNE.setFill('red')
            self.goopie.move(-6, 0)
        elif self.goopie.keyboardQueue.get()['thruster'] == ['NW'] and self.goopie.keyboardQueue.get()['status'] == "On":
            self.goopie.thrusterNW.setFill('red')
            self.goopie.move(6, 0)

        """
        # When thrusters are deactivated
        if self.goopie.keyboardQueue.get()['thruster'] == ['SW', 'SE'] and self.goopie.keyboardQueue.get()[
            'status'] == "Off":
            print('dsfsgsdgsdg')
            self.goopie.thrusterSE.setFill('light grey')
            self.goopie.thrusterSW.setFill('light grey')
            self.goopie.move(0, -3)
        elif self.goopie.keyboardQueue.get()['thruster'] == ['NW', 'NE'] and self.goopie.keyboardQueue.get()[
            'status'] == "Off":
            self.goopie.thrusterNE.setFill('light grey')
            self.goopie.thrusterNW.setFill('light grey')
            self.goopie.move(0, 5)
        elif self.goopie.keyboardQueue.get()['thruster'] == ['NE'] and self.goopie.keyboardQueue.get()[
            'status'] == "Off":
            self.goopie.thrusterNE.setFill('light grey')
            self.goopie.move(-6, 0)
        elif self.goopie.keyboardQueue.get()['thruster'] == ['NW'] and self.goopie.keyboardQueue.get()[
            'status'] == "Off":
            self.goopie.thrusterNW.setFill('light grey')
            self.goopie.move(6, 0)
        """

        self.goopie.keyboardQueue.queue.clear()

    def clearPelletOnContact(self):
        removedPellet = self.goopie.pelletConsumedQueue.get()
        self.goopie.pellets[removedPellet].undraw()
        self.goopie.pellets.pop(removedPellet)