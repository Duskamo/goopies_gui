
from libs.graphics import *

class Tank:
	def __init__(self,win):
		self.win = win

		self.initState()

	def initState(self):
		self.border = Circle(Point(600,400),400)
		self.border.setWidth(10)
		self.border.setOutline('Cyan')

	def draw(self):
		self.border.draw(self.win)
