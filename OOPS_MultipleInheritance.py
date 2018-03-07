# Multilevel inheritance 

class OperatingSystem:
	multitasking = True

class Apple:
	website = 'www.apple.com'

class Macbook(OperatingSystem, Apple):
	def __init__(self):
		if self.multitasking is True:
			print ("This is a multitasking system. Visit {} for more information".format(self.website))

macBook = Macbook()