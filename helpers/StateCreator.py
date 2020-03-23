
import random
from queue import Queue

from Config import *

from models.Tank import *
from models.Zapper import *
from models.Goopie import *
from models.Pellet import *

class StateCreator:
	def __init__(self,win):
		self.win = win

	def createGame(self):
		# make sure objects dont touch
		objectsDontTouch = False
		while not objectsDontTouch:
			# init game object lists
			self.zappers = []
			self.goopies = []
			self.pellets = []

			# generate random coordinates to place objects in tank
			randCoords = []
			for i in range(Config.GOOPIE_POPULATION + Config.ZAPPER_POPULATION + Config.PELLET_POPULATION):
				randCoords.append({'x':random.randint(350,850), 'y':random.randint(150,650)})

			# check to see if all objects are separate
			objCount = 0  
			for i in range(len(randCoords)):
				for j in range(len(randCoords)):
					if ((abs(randCoords[i]['x'] - randCoords[j]['x']) < 125) and (abs(randCoords[i]['y'] - randCoords[j]['y']) < 125)):
						objCount += 1

			if objCount == len(randCoords):
				objectsDontTouch = True
			

		# place objects in tank 
		for i in range(Config.GOOPIE_POPULATION):
			self.goopies.append(Goopie(self.win,randCoords[0]['x'],randCoords[0]['y']))
			randCoords.pop(0)

		for i in range(Config.ZAPPER_POPULATION):
			self.zappers.append(Zapper(self.win,randCoords[0]['x'],randCoords[0]['y']))
			randCoords.pop(0)

		for i in range(Config.PELLET_POPULATION):
			self.pellets.append(Pellet(self.win,randCoords[0]['x'],randCoords[0]['y']))
			randCoords.pop(0)
				
				
		# print objects to tank
		for i in range(len(self.zappers)):
			self.zappers[i].draw()

		for i in range(len(self.goopies)):
			self.goopies[i].draw()

		for i in range(len(self.pellets)):
			self.pellets[i].draw()

	def getZappers(self):
		return self.zappers

	def getGoopies(self):
		return self.goopies

	def getPellets(self):
		return self.pellets
		
	
