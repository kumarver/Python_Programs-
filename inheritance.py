class Employee:
	raise_amt = 1.04
	
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first +'.'+last+'@companyname.com'

	def fullName(self):
		return self.first + ' '+self.last

	def apply_raise(self):
		return int(self.pay * self.raise_amt)

class Developer(Employee):
	raise_amt = 1.10

	def __init__(self,first,last,pay,prog_lag):
		Employee.__init__(self,first,last,pay)
		self.prog_lag = prog_lag

class Manager(Employee):

	def __init__(self,first,last,pay,employees = None):
		Employee.__init__(self,first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)
	
	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_employees(self):
		for emps in self.employees:
			print '--->',emps.fullName()



#emp1 = Employee('Alok','Verma',50000)

#print emp1.email
#print emp1.fullName()
#print emp1.pay
#print emp1.apply_raise()

dev1 = Developer('Alok','Verma',50000,'Python')
dev2 = Developer('Vivek','Verma',60000,'Java')


#print dev1.email
#print dev1.fullName()
#print dev1.prog_lag


mng1 = Manager('Sue','Smith',90000,[dev1])

print mng1.email
print mng1.fullName()

mng1.add_emp(dev2)

mng1.remove_emp(dev2)

mng1.print_employees()
