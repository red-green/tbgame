## main file, yo
## by red-green aka @nwx_hax

import parser
import rooms
from settings import *

currentroom = 1
lastroom = 0

inventory = []

def invweight():
	## total weight of inventory
	w = 0
	for i in inventory:
		w += i.weight
	return w

while True:
	roomc = rooms.rooms.get(currentroom,None)
	rooms.inv(inventory)
	if not roomc:
		print 'oops! room {} doesn\'t exist!'.format(currentroom)
		break
	roomc.printr(lastroom!=currentroom)
	cmd,val = parser.getinput('> ')
	o = roomc.handle((cmd,val))
	lastroom = currentroom
	if o is None:
		## handle movement
		if cmd[:3] == 'go ':
			d = cmd[3:] # direction
			nr = roomc.doors.get(d,None)
			if nr:
				currentroom = nr[1]
			else:
				print "You can't go that way"
		elif cmd == 'quit':
			#if raw_input('are you sure? ')[0] == 'y':
			break
		elif cmd == 'inventory':
			print "You are holding {}".format(', '.join('a ' + i.name for i in inventory))
		elif cmd == 'pick up':
			if val == 'all':
				mv = range(len(roomc.items))
			else:
				mv = []
				for i in val.split(','):
					a = False
					for idx,j in enumerate(roomc.items):
						if j.name == i or i in j.altnames:
							mv.append(idx)
							a = True
							break
					if a == False:
						print "There is no {} in the room".format(i)
			tomove = []
			for ir in mv:
				try:
					i = roomc.items[ir]
				except:
					break
				if invweight() + i.weight <= MAXWEIGHT:
					tomove.append((ir,i))
					print "{}: picked up".format(i.name)
				elif i.weight < MAXWEIGHT:
					print "{}: not a chance".format(i.name)
				else:
					print "{}: your load is too heavy".format(i.name)
			for tm,i in reversed(tomove):
				del roomc.items[tm]
				inventory.append(i)
		elif cmd == 'put down':
			if val == 'all':
				mv = range(len(inventory)-1)
			else:
				mv = []
				for i in val.split(','):
					a = False
					for idx,j in enumerate(inventory):
						if j.name == i or i in j.altnames:
							mv.append(idx)
							a = True
							break
					if a == False:
						print "There is no {} in your inventory".format(i)
			tomove = []
			for ir in mv:
				try:
					i = inventory[ir]
				except:
					break
				if i.canbedropped:
					tomove.append(ir)
					print "{}: dropped".format(i.name)
				else:
					print "{}: cannot be dropped".format(i.name)
			tomove.sort(reverse=True) # make sure we iterate backwards so we don't screw up the list order
			for tm in tomove:
				cl = inventory[tm]
				del inventory[tm]
				roomc.items.append(cl)

		else:
			print "Command not understood"

	elif o is list:
		for act,dat in o:
			if act == 'gotoroom':
				currentroom = dat
