## item classes


class baseitem(object):
	def __init__(self,name='unknown item',weight=10,typ='none',canbedropped=True):
		self.name = name
		self.altnames = name.split()
		self.weight = weight
		self.type = typ
		self.canbedropped = canbedropped



############## base classes

class baselight(baseitem):
	def __init__(self,*args,**kwargs):
		super(self.__class__, self).__init__(*args,**kwargs)
		self.on = kwargs.get('lighton',False)
		self.type = 'light'

class basedoor(baseitem): # perhaps this should not be an item...
	def __init__(self,*args,**kwargs):
		super(self.__class__, self).__init__(*args,**kwargs)
		self.dooropen = kwargs.get('dooropen',False)
		self.weight = 10000000000 # never able to pick up a door
		self.type = 'door'

class basetreasure(baseitem):
	def __init__(self,*args,**kwargs):
		super(self.__class__, self).__init__(*args,**kwargs)
		self.type = 'treasure'


############## specific classes

 #.....
