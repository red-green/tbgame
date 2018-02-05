### room definitions
# not nessecarily rooms tho, just places i guess
import random

from roomdefs import *

inventory = [] # placeholder?
def inv(i):
	global inventory
	inventory = i

def gi(s):
	for i in inventory:
		if i.name == s:
			return True
	return False

def lit():
	for i in inventory:
		if i.type == 'light': # and i.on:
			return True
	return False


rooms = {}

######################################## room 1

class startpoint(baseroom):
	def init(self):
		#### data:
		self.name = 'Forest'
		self.desc = "You awake in a forest, with no memory of who you were or where you came from."
		self.doors = {
			'e':('path',2,True)
		}

rooms[1] = startpoint()

class street1(baseroom):
	def init(self):
		#### data:
		self.name = 'Street'
		self.desc = 'You are at the end of a street'
		self.doors = {
			'w':('path',1,True),
			'n':('road',3,True)
		}

rooms[2] = street1()

class street2(baseroom):
	def init(self):
		#### data:
		self.name = 'Street'
		self.desc = 'You are in the middle of a street. You faintly see buildings to the north.'
		self.doors = {
			's':('road',2,True),
			'n':('road',4,True)
		}

rooms[3] = street2()

class street3(baseroom):
	def init(self):
		#### data:
		self.name = 'Intersection'
		self.desc = 'You find yourself in an intersection in what looks like a ghost town. You have noticed that no cars have passed you on your way down the street.'
		self.doors = {
			's':('road',3,True),
			'e':('rough-looking road',5,True),
			'n':('wide highway stretching into the distance',6,True),
			'w':('dark alleyway',7,True)
		}
		self.items = [
			basetreasure(name='golden ring',weight=1)
		]

rooms[4] = street3()

class estreet1(baseroom):
	def init(self):
		#### data:
		self.name = 'Rough-looking street'
		self.desc = 'Every house you see is boarded up. Some look like they have been burned, others completely destroyed.'
		self.doors = {
			'w':('intersection',4,True),
			'e':('large crater',11,True)
		}

rooms[5] = estreet1()

class estreet2(baseroom):
	def init(self):
		#### data:
		self.name = 'The bottom of a crater'
		self.desc = 'This crater looks very old, like some sort of high explosive went off many years ago. There are a lot of random items spread around.'
		self.doors = {
			'w':('damaged street',5,True)
		}
		self.items = [
			baseitem(name='hammer',weight=25),
			baselight(name='glowing piece of plutonium',weight=60),
			basetreasure(name='piece of paper',weight=1)
		]
	def before(self):
		print lit()

rooms[11] = estreet2()

class alleyway1(baseroom):
	def init(self):
		#### data:
		self.name = 'In an alleyway'
		self.desc = ''
		self.doors = {
			'e':('intersection',4,True),
			'w':('darker alley',12,True),
			'n':('half-open door',13,True)
		}

rooms[7] = alleyway1()

class alleyway2(baseroom):
	def init(self):
		#### data:
		self.name = 'In an alleyway'
		self.desc = ''
		self.doors = {
			'e':('lighter alley',7,True),
			's':('half-open door',14,True)
		}

rooms[12] = alleyway2()

class darkroom1(baseroom):
	def init(self):
		#### data:
		self.name = 'Dark room'
		self.desc = 'You can barely see in here without some sort of light source'
		self.doors = {
			's':('half-open door',7,True),
			'nw':('stairway',15,lit())
		}

rooms[13] = darkroom1()

class darkroom3(baseroom):
	def init(self):
		#### data:
		self.name = 'Another dark room'
		self.desc = 'You can barely see in here'
		self.doors = {
			'sw':('stairway',13,lit())
		}
		self.items = [
			basetreasure(name='large key',weight=4)
		]

rooms[15] = darkroom3()

class highway1(baseroom):
	def init(self):
		#### data:
		self.name = 'Middle of the highway'
		self.desc = 'You are several miles down the highway. The forest has given way to a dry plain.'
		self.doors = {
			's':('town, barely visible',4,True),
			'n':('long stretch of highway',8,True)
		}

rooms[6] = highway1()

class highway2(baseroom):
	def init(self):
		#### data:
		self.name = 'Middle of the highway'
		self.desc = 'You are so far down the highway that the town is out of sight. You start to feel tired.'
		self.doors = {
			's':('highway',8,True),
			'n':('stretch of highway',9,True)
		}

rooms[8] = highway2()

class highway3(baseroom):
	def init(self):
		#### data:
		self.name = 'End of the highway'
		self.desc = 'You find that the highway goes through a gate in a chain link fence. Because of razor wire, you are unable to climb the fence. There is, however, a padlock on the gate. If only you had a key...'
		self.doors = {
			's':('highway',9,True)
		}
		self.gate_unlocked = False
	def after(self,cmd):
		key = gi('large key')
		if cmd[0] in ['go n','climb'] and not self.gate_unlocked:
			if key:
				print 'Perhaps try unlocking the gate...'
			else:
				print random.choice(['Your attempts to defeat the fence are unsuccessful','You try to scale the fence, but cut yourself','The razor wire at the top of the fence is enough to convince you otherwise'])
			return True
		if cmd[0] == 'unlock':
			if key and not self.gate_unlocked:
				print 'The lock is rusty, but you manage to pop it open. As the chain falls to the ground, you push the gate open and walk past the fence.'
				self.name = 'Gate in highway'
				self.desc = 'The highway passes through an open gate in a large chain-link fence.'
				self.doors['n'] = ('open gate',10,True)
				self.gate_unlocked = True
			elif self.gate_unlocked:
				print 'You have already opened the gate.'
			else:
				print 'You have no key with which to unlock the gate, and your lock picking skills aren\'t adequate to defeat the padlock.'
			return True

rooms[9] = highway3()

class highway4(baseroom):
	def init(self):
		self.name = "A fork in the road"


rooms[10] = highway4()


class canyon2(baseroom):
	def init(self):
		self.name = "A narrow section of canyon"
		self.desc = "The canyon converges and there is a narrow space to walk through. In the middle of this area, there is a button on a wall and some red dust on the floor next to it."
		self.doors = {
			's':('wide canyon',19,True),
			'n':('narrower canyon',21,True)
		}
	def after(self,cmd):
		if cmd[0] == 'press button':
			print 'You press the button. The red dust lights up briefly and then a piston smashes you in the face and you suffocate inside the wall of the canyon.'
			print 'You died. RIP'
			return [('gotoroom',1001)]



class heaven1(baseroom):
	def init(self):
		self.name = "Heaven lobby"
		self.desc = "A lobby made of what looks like clouds. There are many chairs but nobody is waiting in them"
		self.doors = {
			'w':('set of pearly gates',1002,True),
			'ne':('broom closet',1003,True)
		}
		self.items = [
			basetreasure(name='moonstone key', weight=10),
			baseitem(name='cloud balloon', weight=-20)
		]
rooms[1001] = heaven1()

class heaven2(baseroom):
	def init(self):
		pass

rooms[1002] = heaven2()

class heavencloset1(baseroom):
	def init(self):
		self.name = "Heavenly broom closet"
		self.desc = "It appears to be a closet for the janitors of this place, whomever they are. Unlike the lobby, this closet is quite dark."
		self.doors = {
			'sw':('door to the lobby',1001,True),
			'u':('air vent',1004,lit())
		}

rooms[1003] = heavencloset1()

class heavenduct1(baseroom):
	def init(self):
		self.name = "Ventilation duct"
