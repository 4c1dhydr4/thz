class Father(object):
	def hello(self):
		print('hello')

class Son(Father):
	def goodbye(self):
		print('Goodbye')


son = Son()

son.hello()
