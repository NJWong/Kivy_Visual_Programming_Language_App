from kivy.uix.button import Button
from kivy.properties import BooleanProperty

class GoalTile(Button):
	'''
	A simple Goal tile entity that inherits from Button.
	NOTE: The code below does not justify an entire class dedicated
	to a clear tile. It is expected that the complexity of this class
	in the future warrants a dedicated class.
	'''
	collide = BooleanProperty(False)