
import random
import math
from libs.graphics import *

from managers.ZapperUpdateManager import *

from Config import *

class Zapper:
	def __init__(self,win,x,y):
		self.win = win
		self.x = x
		self.y = y
		self.radius = 50

		self.updateManager = ZapperUpdateManager(self)
		self.speed = 0.1

		self.initState()


	def initState(self):
		self.body = Circle(Point(self.x,self.y),self.radius)
		self.body.setWidth(10)
		self.body.setOutline('Cyan')

		self.center = Rectangle(Point(self.x-20,self.y-20),Point(self.x+20,self.y+20))
		self.center.setFill('Cyan')

	def draw(self):
		self.body.draw(self.win)
		self.center.draw(self.win)

	def undraw(self):
		self.body.undraw()
		self.center.undraw()

	def move(self,dx,dy):
		self.x = self.x + dx
		self.y = self.y + dy

		self.body.move(dx, dy)
		self.center.move(dx, dy)

	def update(self):
		# move zapper randomly
		if Config.ZAPPER_MOVEMENT == "Random":
			self.updateManager.zapperMoveRandom()

		# move zapper with knowledge of goopies whereabouts
		elif Config.ZAPPER_MOVEMENT == "Nearest":
			self.updateManager.zapperMoveNearestGoopie()