
from libs.graphics import *

class Pellet:
	def __init__(self,win,x,y):
		self.win = win
		self.x = x
		self.y = y 
		self.radius = 10

		self.initState()


	def initState(self):
		self.body = Circle(Point(self.x,self.y),self.radius)
		self.body.setWidth(1)
		self.body.setFill('yellow')

		self.core = Rectangle(Point(self.x-5,self.y-5),Point(self.x+5,self.y+5))
		self.core.setWidth(1)
		self.core.setFill('black')
		

	def draw(self):
		self.body.draw(self.win)
		self.core.draw(self.win)
