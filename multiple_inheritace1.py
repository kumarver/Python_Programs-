class Person:
	def __init__(self,personName,personAge):
		self.name=personName
		self.age=personAge
	def showName(self):
		print self.name
	def showAge(self):
		print self.age

class StudentID:
	def __init__(self,studentId):
		self.studentID = studentId
	def getID(self):
		return self.studentID

class Resident(Person,StudentID):
	def __init__(self,name,age,id):
		Person.__init__(self,name,age)
		StudentID.__init__(self,id)

res = Resident('Alok',24,'verma.alok606@gmail.com')
res.showName()
res.showAge()
print res.getID()

