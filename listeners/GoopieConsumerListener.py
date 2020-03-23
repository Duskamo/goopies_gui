
import threading
import time

class GoopieConsumerListener(threading.Thread):
	def __init__(self,goopies):
		super(GoopieConsumerListener, self).__init__()
		self.goopies = goopies

	def run(self):
		while True:
			for i in range(len(self.goopies)):
				# determine if goopies consumed a pellet or not
				if self.goopieConsumedPellet():
					self.goopies[i].health += 20
				else:
					self.goopies[i].health -= 1

				# change goopie state as health increases or decreases
				if self.goopies[i].health >= 70:
					self.goopies[i].color = 'Blue'
				elif self.goopies[i].health >= 30 and self.goopies[i].health < 70:
					self.goopies[i].color = 'Yellow'
				elif self.goopies[i].health < 30:
					self.goopies[i].color = 'Red'

			time.sleep(0.25)

	
	def goopieConsumedPellet(self):
		return False
