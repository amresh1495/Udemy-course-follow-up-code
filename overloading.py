# overloading can be achieved using special methods starting with __

class Square:
	def __init__(self, side):
		self.side = side 

	def __add__(squareOne, squareTwo):
		return ((4 * squareOne.side) + (4 * squareTwo.side))

squareOne = Square(5)
squareTwo = Square(10)

print ("The sum of sides of both the squares is :", squareOne + squareTwo)