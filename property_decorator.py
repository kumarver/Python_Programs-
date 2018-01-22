#Using the property decoratot we can use the Class method as Attribute
class Employee:
	raise_amt = 1.04
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
#		self.email = first + '.'+ last + '@email.com'
	@property
	def email(self):
		return self.first+'.'+self.last+'@email.com'

	def fullname(self):
		return self.first + ' '+ self.last


emp = Employee('Alok','Verma',50000)

emp.first = 'Anjan'
emp.last = 'Das'
emp.pay = 50000

print emp.first
print emp.email
print emp.fullname()
