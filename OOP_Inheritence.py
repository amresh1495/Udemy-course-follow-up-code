# single level inheritence

class Apple:
	manufacturer = 'Apple Inc.'
	contactWebsite = 'www.apple.com/contact'

	def contactDetails(self):
		print ("To contact us, log on to ", self.contactWebsite)

class Macbook(Apple):
	def __init__(self):
		self.yearOfManufacture = 2017

	def manufactureDetails(self):
		print ("This macbook was manufactured by in the year {} by {}".format(self.yearOfManufacture, self.manufacturer))

obj = Macbook()
obj.manufactureDetails()
obj.contactDetails()