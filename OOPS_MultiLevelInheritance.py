# multilevel inheritance 

class MusicalInstruments:
	numberOfKeys = 12

class Strings(MusicalInstruments):
	typeOfWood = 'Tonewood'

class Guitar(Strings):
	numberOfStrings = 6
	def __init__(self):
		print ("This Guitar has {} strings, it is made of {}, and has {} keys".format(self.numberOfStrings, self.typeOfWood, self.numberOfKeys))

obj = Guitar()