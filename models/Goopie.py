
from libs.graphics import *

from Config import *
from managers.GoopieUpdateManager import *

class Goopie:
	def __init__(self,win,x,y):
		self.win = win
		self.x = x
		self.y = y 
		self.radius = 15

		self.updateManager = GoopieUpdateManager(self)
		self.health = 100
		self.color = 'blue'

		self.initState()

	def initState(self):
		self.body = Circle(Point(self.x,self.y),self.radius)
		self.body.setWidth(1)
		self.body.setOutline(self.color)

		self.gland = Oval(Point(self.x-5,self.y-13),Point(self.x+5,self.y+13))
		self.gland.setWidth(1)
		self.gland.setFill('purple')

		self.sensorNorth = Line(Point(self.x,self.y-20),Point(self.x,self.y-15))
		self.sensorNorth.setFill('red')
		self.sensorSouth = Line(Point(self.x,self.y+20),Point(self.x,self.y+15))
		self.sensorSouth.setFill('red')
		self.sensorWest = Line(Point(self.x-20,self.y),Point(self.x-15,self.y))
		self.sensorWest.setFill('red')
		self.sensorEast = Line(Point(self.x+20,self.y),Point(self.x+15,self.y))
		self.sensorEast.setFill('red')

		self.thrusterNE = Line(Point(self.x,self.y-15),Point(self.x+15,self.y))
		self.thrusterNE.setFill('light grey')
		self.thrusterNW = Line(Point(self.x,self.y-15),Point(self.x-15,self.y))
		self.thrusterNW.setFill('light grey')
		self.thrusterSE = Line(Point(self.x, self.y + 15), Point(self.x + 15, self.y))
		self.thrusterSE.setFill('light grey')
		self.thrusterSW = Line(Point(self.x,self.y+15),Point(self.x-15,self.y))
		self.thrusterSW.setFill('light grey')	

	def draw(self):
		self.body.draw(self.win)
		self.gland.draw(self.win)
		self.sensorNorth.draw(self.win)
		self.sensorSouth.draw(self.win)
		self.sensorWest.draw(self.win)
		self.sensorEast.draw(self.win)
		self.thrusterNE.draw(self.win)
		self.thrusterSE.draw(self.win)
		self.thrusterNW.draw(self.win)
		self.thrusterSW.draw(self.win)

	def undraw(self):
		self.body.undraw()
		self.gland.undraw()
		self.sensorNorth.undraw()
		self.sensorSouth.undraw()
		self.sensorWest.undraw()
		self.sensorEast.undraw()
		self.thrusterNE.undraw()
		self.thrusterSE.undraw()
		self.thrusterNW.undraw()
		self.thrusterSW.undraw()

	def move(self,dx,dy):
		self.x += dx
		self.y += dy		

		self.body.move(dx,dy)
		self.gland.move(dx,dy)
		self.sensorNorth.move(dx,dy)
		self.sensorSouth.move(dx,dy)
		self.sensorWest.move(dx,dy)
		self.sensorEast.move(dx,dy)
		self.thrusterNE.move(dx,dy)
		self.thrusterSE.move(dx,dy)
		self.thrusterNW.move(dx,dy)
		self.thrusterSW.move(dx,dy)
		
	def update(self):
		# Update Skin of goopie by its health
		if self.health > 0:
			self.updateManager.updateSkin()

		# Turn goopie to corpse if health drops to 0
		if self.health == 0:
			self.updateManager.goopieCorpse()

		# Move goopie on keyboard input in basic cardinal direction pattern
		if not self.keyboardQueue.empty() and Config.GOOPIE_MOVEMENT == "Cardinal":
			self.updateManager.goopieKeyboardInput()

		# Move goopie on keyboard input in fluid direction pattern
		if not self.keyboardQueue.empty() and Config.GOOPIE_MOVEMENT == "Fluid":
			self.updateManager.goopieKeyboardInputFluid()

		# Clear pellet from screen when collided
		if not self.pelletConsumedQueue.empty():
			self.updateManager.clearPelletOnContact()
