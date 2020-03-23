
import random
from libs.graphics import *

class Zapper:
	def __init__(self,win,x,y):
		self.win = win
		self.x = x
		self.y = y
		self.radius = 50

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

	def update(self):
		# move zapper randomly
		x = random.randint(-1,1)
		y = random.randint(-1,1)

		self.body.move(x,y)
		self.center.move(x,y)
