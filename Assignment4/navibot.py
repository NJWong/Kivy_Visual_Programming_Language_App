# Import other python classes
from interpreter import *
from programblock import *
from cleartile import *
from walltile import *
from goaltile import *
from navimaze import *
from naviprogram import *
from naviblocks import *
from navicontrols import *
from robot import *
from input_filter import *

# Import kivy functionality
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.clock import Clock
from functools import partial

class NaviBot(FloatLayout):
	'''
	The main class that controls the flow of the application. Implemented as a Kivy FloatLayout Widget.
	Takes the program defined in NaviProgram and passes it statement by statement to the Interpreter
	for execution. Application state (maze, robot location, etc.) is then modified from here.
	'''
	naviprogram = ObjectProperty(None)
	navicontrols = ObjectProperty(None)
	navimaze = ObjectProperty(None)
	interpreter = Interpreter()
	execution_tree = ListProperty(None)
	input_filter = ObjectProperty(None)
	input_filter_tf = ObjectProperty(None)
	input_filter_tf_comma = ObjectProperty(None)
	python_code = StringProperty('')
	
	def run_program(self, program):
		'''
		Take the program defined in NaviProgram and pass it to the interpreter to genererate python code.
		'''
		self.python_code = self.interpreter.interpret(program)

		#print(self.python_code)

		self.execute_program(self.python_code)

	def execute_program(self, python_code):
		'''
		Take the python code generated by the interpreter and execute it
		'''
		try:
			exec(self.python_code)
		except SyntaxError:
			print('you have syntax errors!')

	# OBSOLETE
	def old_run_program(self, program):
		'''
		Take the program defined in NaviProgram and pass it to the interpreter to run.
		'''
		self.execution_tree = self.interpreter.create_execution_tree(self.naviprogram.program)
		
		# Setting up a clock schedule for each statement so there is a visible delay between statement execution.
		for i in range(len(self.execution_tree)):
			try:
				Clock.schedule_once(partial(self.run, self.execution_tree[i]), i)
			except KeyError:
				print('Unknown statement: skipping execution')

	# OBSOLETE
	def run(self, statement, dt):
		'''
		Each statement that the interpreter evaluates returns as a function to modify application state.
		This function is then executed here.
		'''
		exec(statement)

class NaviBotApp(App):
	def build(self):
		navibot = NaviBot()
		navibot.navimaze.initialize()
		return navibot

if __name__ == '__main__':
	NaviBotApp().run()