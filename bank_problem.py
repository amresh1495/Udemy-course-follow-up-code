
# a simple banking system implemented in python 

from abc import ABCMeta, abstractmethod
from random import randint

class Accounts(metaclass = ABCMeta):

	@abstractmethod
	def createAccount():
		return 0

	@abstractmethod
	def authenticate():
		return 0

	@abstractmethod
	def deposit():
		return 0

	@abstractmethod
	def withdraw():
		return 0

	@abstractmethod
	def displayAmount():
		return 0


class SavingsAccount(Accounts):

	def __init__(self):
		# [key][0] => name ; [key][1] => initial deposit / balance 
		self.savingsAccount = {}

	def createAccount(self, name, initialDeposit):
		self.accountNumber = randint(10000, 99999)
		self.savingsAccount[self.accountNumber] = [name, initialDeposit]
		print ("Account successfully created. Account number is : ", self.accountNumber)

	def authenticate(self, name, accountNumber):
		if accountNumber in self.savingsAccount.keys():
			if self.savingsAccount[accountNumber][0] == name:
				print ("Authentication successful")
				self.accountNumber = accountNumber
				return True 
			else:
				print ("Authentication failed")
				return False
		else:
			print ("Authentication failed")
			return False

	def deposit(self, depositAmount):
		self.savingsAccount[accountNumber][1] += depositAmount
		self.displayAmount()

	def withdraw(self, withdrawAmount):
		if withdrawAmount > self.savingsAccount[accountNumber][1]:
			print ("Insufficient balance")
		else:
			self.savingsAccount[accountNumber][1] -= withdrawAmount
			self.displayAmount()

	def displayAmount(self):
		print ("Account balance is : ", self.savingsAccount[self.accountNumber][1])

savingsAccount = SavingsAccount()

while True:
	print ("Enter 1 to create a new account")
	print ("Enter 2 to access existing account")
	print ("Enter 3 to exit")

	userchoice = int(input())
	if userchoice is 1:
			print ("Enter your name : ")
			name = input()
			print ("Enter the initial deposit : ")
			deposit = input()
			savingsAccount.createAccount(name, deposit)
	elif userchoice is 2:
		print ("Enter your name : ")
		name = input()
		print ("Enter your account number : ")
		accountNumber = int(input())
		authenticationStatus = savingsAccount.authenticate(name, accountNumber)
		if authenticationStatus is True:
			while True:
				print ("Enter 1 to withdraw")
				print ("Enter 2 to deposit")
				print ("Enter 3 to view account balance")
				print ("Enter 4 to go back to the previous menu")
				userchoice = int(input())
				if userchoice is 1:
					print ("Enter the amount you want to withdraw : ")
					withdrawAmount = input()
					savingsAccount.withdraw(withdrawAmount)
				elif userchoice is 2:
					print ("Enter the amount that you want to deposit : ")
					depositAmount = int(input())
					savingsAccount.deposit(depositAmount)
				elif userchoice is 3:
					savingsAccount.displayAmount()
				elif userchoice is 4:
					break
	elif userchoice is 3:
		quit()
