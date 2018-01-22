class Employee:
	raise_amt = 1.04
	#Constructor
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last+'@componyname.com'
	# Full name Method
	def fullName(self):
		return self.first + ' ' + self.last

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls,amt):
		cls.raise_amt = amt

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str1.split('-')
		return cls(first,last,pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		else:
			return True

emp1 = Employee('alok','verma',50000)
emp2 = Employee('vivek','verma',6000)

#print emp1.first
#print emp2.first
#print emp2.email

#Employee.set_raise_amt(1.05)

#print Employee.raise_amt
#print emp1.raise_amt
#print emp2.raise_amt

#emp_str1 = 'John-Doe-70000'
#first,last,pay = emp_str1.split('-')

new_emp = Employee.from_string(emp_str1)

print new_emp.email
print new_emp.pay

import datetime
mydate = datetime.date(2018,1,6)
print Employee.is_workday(mydate)

