class Chain(object):
	def __init__(self, path = ''):
		self._path = path
		print('init   : self.path= %-26s, path= %s' %(self._path, path))

	def __getattr__(self, path):
		print('getattr: self.path= %-26s, path= %s' %(self._path, path))
		return Chain('%s/%s' %(self._path, path))

	def __str__(self):
		print('str    : self.path= %-26s' %(self._path))
		return self._path

	__repr__ = __str__

