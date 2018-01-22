class A:
	def add_nums(self,a,b):
		return a+ b
class B:
	def add_nums(self,a,b,c):
		return a + b + c

a = A()
print a.add_nums(2,3)
b = B()
print b.add_nums(2,3,4)
