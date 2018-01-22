'''
class Person:
	def __init__(self,personName,personAge):
		self.name=personName
		self.age=personAge

	def showName(self):
		print self.name

	def showAge(slef):
		print self.age

class Student:
	def __init__(self,studentId):
		self.studentId = studentId

	def getID(self):
		return self.studentId

class Resident(Person,Student):
	def __init__(self,name,age,id):
		Person.__init__(self,name,age)
		Student.__init__(self,id)

res = Resident('Alok',25,'averma@infoblox.com')
res.showName()
print res.getID()
'''

class Person:
	def __init__(self,personName,personAge):
		self.name = personName
		self.age = personAge
	def showName(self):
		print self.name
	def showAge(self):
		print self.age

class Student:
	def __init__(self,studentID):
		self.ID = studentID
	def getID(self):
		return self.ID

class Resident(Person,Student):
	def __init__(self,name,age,id):
		Person.__init__(self,name,age)
		Student.__init__(self,id)

res = Resident('Alok',25,'averma@gmail.com')
res.showName()
res.showAge()
print res.getID()

