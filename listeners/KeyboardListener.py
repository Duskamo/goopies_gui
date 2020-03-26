import time
from pynput import keyboard
from functools import partial

from Config import *

class KeyboardListener:
	def __init__(self,keyboardQueue):
		self.listener = None
		self.keyboardQueue = keyboardQueue

		self.current = set()

	def join(self):
		# Collect events until released
		with keyboard.Listener(
			on_press=self.on_press,
			on_release=self.on_release) as listener:
			listener.join()

	def start(self):
		# ...or, in a non-blocking fashion:
		self.listener = keyboard.Listener(
		    on_press=partial(self.on_press))
		self.listener.start()

	def on_press(self,key):
		if Config.GOOPIE_MOVEMENT == "Cardinal":
			try:
				if key == keyboard.Key.up:
					self.keyboardQueue.put("Up")
				elif key == keyboard.Key.down:
					self.keyboardQueue.put("Down")
				elif key == keyboard.Key.left:
					self.keyboardQueue.put("Left")
				elif key == keyboard.Key.right:
					self.keyboardQueue.put("Right")

			except AttributeError:
				print('special key {0} pressed'.format(key))
		elif Config.GOOPIE_MOVEMENT == "Fluid":
			try:
				if key == keyboard.Key.up:
					self.keyboardQueue.put({'thruster':['SW','SE'], 'status':'On'})
				elif key == keyboard.Key.down:
					self.keyboardQueue.put({'thruster':['NW','NE'], 'status':'On'})
				elif key == keyboard.Key.left:
					self.keyboardQueue.put({'thruster':['NE'], 'status':'On'})
				elif key == keyboard.Key.right:
					self.keyboardQueue.put({'thruster':['NW'], 'status':'On'})

			except AttributeError:
				print('special key {0} pressed'.format(key))
	"""
	def on_release(self, key):
		if Config.GOOPIE_MOVEMENT == "Fluid":
			try:
				if key == keyboard.Key.up:
					self.keyboardQueue.put({'thruster': ['SW', 'SE'], 'status': 'Off'})
				elif key == keyboard.Key.down:
					self.keyboardQueue.put({'thruster': ['NW', 'NE'], 'status': 'Off'})
				elif key == keyboard.Key.left:
					self.keyboardQueue.put({'thruster': ['NE'], 'status': 'Off'})
				elif key == keyboard.Key.right:
					self.keyboardQueue.put({'thruster': ['NW'], 'status': 'Off'})

			except AttributeError:
				print('special key {0} pressed'.format(key))
	"""