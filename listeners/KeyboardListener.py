import time
from pynput import keyboard
from functools import partial

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

