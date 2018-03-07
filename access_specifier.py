# public => memberName
# protected => _memberName
# private => __memberName

class car:
	nameOfCar = 'Tesla Roadster 2020'
	_color = 'Red'
	__yearOfManufacture = 2020  # saved as _car__yearOfManufacture - can be used outside class if neccesary - even being private
                                # this is called name mangling 
    
class spacex(car):
	def __init__(self):
		print ("Protected attribute : ", self._color)

car = car()
print ("Public attribute : ", car.nameOfCar)
spacex = spacex()
print ("Accessing private attribute: ", car._car__yearOfManufacture)  # accessing private attribute outside the class 