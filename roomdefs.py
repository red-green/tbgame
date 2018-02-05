## putting this in another file for sanity

"""
example:

class room1(baseroom):
	def init(self):
		#### data:
		self.name = 'Forest'
		self.desc = ''
		self.doors = {
			'n':('path',2,True)
		}

	def before(self):
		## called before the command is inputted, useful for pointing out stuff in the room dynamically

	def after(self,cmd):
		## called before command is parsed, if any special commands are valid in this room
		## return None to continue parsing commands, True to stop parsing, and a list of tuples to execute some commands

rooms[1] = room1()


id: room id number
doors:
dict of direction:(type, other room number, visible)
invisible doors should have a lambda function in the visible spot
directions: n,s,e,w,ne,nw,se,sw,u,d

each room handler function will return a list of commands to be executed by the main game
if the handle function returns None, the main game will instead parse the command
command sent ot handle are a 2-tuple of (normalized verb, rest of sentence)
"""

from items import *


class baseroom:
	init = None
	before = None
	after = None

	def __init__(self):
		self.name = 'Undefined'
		self.desc = 'Clearly, the author of this code didn\'t intend for you to end up here...'
		self.doors = {
			'u':('portal back to the start',1,True)
		}
		self.items = []
		#### other stuff:
		self.displayfull = True
		if self.init:
			self.init()

	def printr(self,l):
		## called before input
		if self.displayfull:
			printroom(self,3)
			self.displayfull = False
		elif l:
			printroom(self,2)
		else:
			printroom(self,1)
		self.before()

	def handle(self,cmd):
		if cmd[0] == 'look':
			self.displayfull = True
			return True
		return self.after(cmd)

	def after(self,cmd):
		return None
	def before(self):
		return None

############################## other things:

directions = {
'n':'To the north',
's':'To the south',
'e':'To the east',
'w':'To the west',
'ne':'To the northeast',
'nw':'To the northwest',
'se':'To the southeast',
'sw':'To the southwest',
'u':'Above you',
'd':'Below you'
}

def printroom(dat,full=3):
	if full>1:
		print "{}".format(dat.name)
	if full>2:
		print dat.desc
		for d in dat.doors:
			print "{}, there is a {}".format(directions.get(d,'Also'),dat.doors[d][0])
		for i in dat.items:
			print "There is a {} here".format(i.name)
