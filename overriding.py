# OOP - Overriding 
# can be overcome using super()

class employee:
	def numberOfWorkingHours(self):
		self.numberOfWorkingHours = 40
		
	def displayNumberOfWorkingHours(self):
		print (self.numberOfWorkingHours)

class trainee(employee):
	def numberOfWorkingHours(self):
		self.numberOfWorkingHours = 45  # this will ovrride the method in base class 

	def resetNumberOfWorkingHours(self):
		super().numberOfWorkingHours()  # this will transfer the control back to the base class thereby overcoming overrriding 

employee = employee()
employee.numberOfWorkingHours()
print ("Number of working hours for employees are :", end = ' ')
employee.displayNumberOfWorkingHours()

trainee = trainee()
trainee.numberOfWorkingHours()
print ("Number of working hours for trainees are :", end = ' ')
trainee.displayNumberOfWorkingHours()
print ("Number of working hours for trainees are :", end = ' ')
trainee.resetNumberOfWorkingHours()
trainee.displayNumberOfWorkingHours()
