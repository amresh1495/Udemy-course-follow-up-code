# Python code follow up on udemy course - The four pillars of object oriented programming in python

# check if an employee has achieved his weekly target - 

class Employee:

	"""attributes like name, designation etc are included 
	below to help understand more about the class"""

	name = 'Amresh'   
	designation = 'Salesman'
	salesMadeThisWeek = 6

	def salesAchieved(self):
		if self.salesMadeThisWeek >= 5:
			print ("Target has been achieved")
		else:
			print ("Target has not been achieved")

# creating ojbect for Employee class 
EmployeeOjb = Employee() 

# accesssing the class attribute using the class object that we created 
print (EmployeeOjb.name)  

# accessing the class method using the class object 
print (EmployeeOjb.salesAchieved())

# new class telling more about attributes - they must be same for all objects for access 

class employee2:
	numberOfWorkingHours = 40 

employee2obj = employee2()
employee2obj2 = employee2()

# created two objects for the same class and accessed the class attribute and printed it below 
# the value of class attribute remains the same for all objects 
print (employee2obj.numberOfWorkingHours)  
print (employee2obj2.numberOfWorkingHours)

# we can also update the attribute of class 
employee2.numberOfWorkingHours = 45

# accessing and printing the updated class attribute using object of that class 
print (employee2obj.numberOfWorkingHours)

# making an instance attribute - these are different for different objects 
employee2obj.name = 'Amresh Giri'
print (employee2obj.name)

# print (employee2obj2.name) this will give attribute error because it 'name' can't be accessed by other object 

# we create different attribute for different oject 
employee2obj2.name = 'Giri Amresh'
print (employee2obj2.name)

# we can create instance attribute of a class attribute for a particular object 
# the interpreter first checks for the instance attribute, then looks for class attribute 
employee2obj.numberOfWorkingHours = 50
print (employee2obj.numberOfWorkingHours) # -> O/P = 50 because instance attribute changed to 50 so it will be reflected

# therefore, we can change the class attribute for a particular oject but that won't change its value in the class, it will 
# change it in the instance attribute of that object 


# Self parameter 

class employee3:
	def employeeDetails(self):  # -> self here is an object for creating class instance 'name'
		self.name = 'Amresh Giri'
		print ('Name : ', self.name)
		age = 22
		
	def printEmployeeDetails(self):
		print ('Age : ', age)

	@staticmethod	
	def staticMethodDemo():
		print ("Welcome to our organization !")

emp3ojb = employee3()

# calling the class method unconventionally - by passing object of the class 
employee3.employeeDetails(emp3ojb)
		
# calling the class methos using more conventional way using just the object
emp3ojb.employeeDetails()

# calling the printEmployeeDetails method 
#emp3ojb.printEmployeeDetails()  # --> this gives error - age not accessible because no instance has been defined for it hence
								 #	it can't be accessed outside the method - it's scope is limited

# we can avoid using self if not needed by using @staticmethod - when we don't need to use self 
emp3ojb.staticMethodDemo()

# use of init() method - used for initialising the class attributes which are shared by methods 
# it is the first method to be invoked in the class


class emp4:

	def __init__(self):
		self.name = 'AMRESH GIRI'

	def accessDetail(self):
		print (self.name)

emp4obj = emp4()

# calling the method accessDetail and accessing already initialized attribute 
emp4obj.accessDetail()


class library:

	def __init__(self):
		self.bookCount = 100

	def borrow(self):
		print ("Do you want to borrow a book ?")
		x = input()
		if x == 'yes' or x == 'YES':
			self.bookCount-=1

	#@staticmethod
	def update(self):
		print ("The number of books currently in the library are : ", self.bookCount)

libObj = library()

libObj.borrow()
libObj.update()



