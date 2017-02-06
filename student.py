class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' %(self.__name, self.__score))

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		self.__score = score


	@property
	def score(self):
		return self.__score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('somce must between 0 ~ 100!')
		self.__score = value


	@property
	def birth(self):
		return self.__birth

	@birth.setter
	def birth(self, value):
		self.__birth = value

	@property
	def age(self):
		return 2016 - self.__birth


	def __getattr__(self, attr):
		if attr == 'gender':
			return 'male'




