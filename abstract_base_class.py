
from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta):
	@abstractmethod
	def area(self):
		return 0


class Square(Shape):
	def area(self):
		self.side = 4
		print ("Area of square :", self.side * self.side)

class Rectanlge(Shape):
	def area(self):
		self.width = 5
		self.length = 10
		print ("Area of the rectangle is : ", self.width * self.length)

square = Square()
rectangle = Rectanlge()

square.area()
rectangle.area()