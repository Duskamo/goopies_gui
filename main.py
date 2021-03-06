
import time
from libs.graphics import *
from queue import Queue

from models.Tank import *
from models.Zapper import *
from models.Goopie import *
from models.Pellet import *

from helpers.StateCreator import *
from listeners.GoopieConsumerListener import *
from listeners.KeyboardListener import *

class main():
	def __init__(self):
		self.initialize()

	def initialize(self):
		# Setup Background, game objects, and initial states
		self.win = GraphWin('Goopies', 1200, 800)
		self.win.setBackground('black')

		self.tank = Tank(self.win)
		self.tank.draw()

		self.stateCreator = StateCreator(self.win)
		self.stateCreator.createGame()
		self.goopies = self.stateCreator.getGoopies()
		self.pellets = self.stateCreator.getPellets()
		self.zappers = self.stateCreator.getZappers()

		self.isRunning = True

		# Setup Queues, Listeners, and off threads
		self.keyboardQueue = Queue(maxsize=0)
		self.pelletConsumedQueue = Queue(maxsize=0)

		self.goopies[0].pellets = self.pellets
		self.goopies[0].keyboardQueue = self.keyboardQueue  # TEMP
		self.goopies[0].pelletConsumedQueue = self.pelletConsumedQueue

		goopieConsumerListener = GoopieConsumerListener(self.goopies,self.pellets,self.pelletConsumedQueue)
		goopieConsumerListener.start()
		keyboardListener = KeyboardListener(self.keyboardQueue)
		keyboardListener.start()

		# Setup Game Loop
		self.run()

		# Pause and Close
		self.win.getMouse() 
		self.win.close() 

	def run(self):	
		# Game Loop
		while self.isRunning:
			# Process Events - Process inputs and other things
			self.processEvents()

			# Update - Update all objects that needs updating, ex position changes, physics
			for i in range(len(self.goopies)):
				self.goopies[i].update()

			for i in range(len(self.zappers)):
				self.zappers[i].goopies = self.goopies
				self.zappers[i].update()

			# Draw - Render things on screen

			# Pause thread for framerate
			time.sleep(0.0017)

	def processEvents(self):
		# Check if game is complete or not
		""


if __name__ == "__main__":
	main = main()
