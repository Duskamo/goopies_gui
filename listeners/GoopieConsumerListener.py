
import threading
import time

class GoopieConsumerListener(threading.Thread):
	def __init__(self,goopies,pellets,pelletConsumedQueue):
		super(GoopieConsumerListener, self).__init__()
		self.goopies = goopies
		self.pellets = pellets
		self.pelletConsumedQueue = pelletConsumedQueue

	def run(self):
		while True:
			for i in range(len(self.goopies)):
				# determine if goopies consumed a pellet or not
				if self.goopieConsumedPellet(i):
					self.goopies[i].health += 20
				else:
					""
					#self.goopies[i].health -= 1

				# change goopie state as health increases or decreases
				if self.goopies[i].health >= 70:
					self.goopies[i].color = 'Blue'
				elif self.goopies[i].health >= 30 and self.goopies[i].health < 70:
					self.goopies[i].color = 'Yellow'
				elif self.goopies[i].health < 30:
					self.goopies[i].color = 'Red'

				#print(i, self.goopies[i].health)

			time.sleep(0.25)

	
	def goopieConsumedPellet(self,i):
		isPelletConsumed = False
		for j in range(len(self.pellets)):
			if (abs(self.goopies[i].x - self.pellets[j].x) < 20) and (abs(self.goopies[i].y - self.pellets[j].y) < 20):
				isPelletConsumed = True
				self.pelletConsumedQueue.put(j)

		return isPelletConsumed
