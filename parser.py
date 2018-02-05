## parser

import commands

rvaliases = {}
## generate replacement dicts
for i in commands.valiases:
	for j in i:
		rvaliases[j] = i[0]

def startswith(s,p):
	p += ' ' # prevents parts of words
	return s[:len(p)] == p

def verbalias(s):
	for i in rvaliases.keys():
		if startswith(s,i):
			return rvaliases.get(i,''),i
	return '',''

def getinput(ch):
	try:
		a = raw_input(ch) + ' '
	except:
		a = 'quit '
		print
	v,k = verbalias(a)
	c = a.replace(k,'')
	return v,c.strip()
