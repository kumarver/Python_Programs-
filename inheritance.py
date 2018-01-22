class A1:
	def who_am_i(self):
		print 'I am A1'
class A2:
	def who_am_i(self):
		print 'I am A2'
class A3(A1):
	def who_am_i(self):
		print 'I am A3'
class B(A2,A3):
#	def who_am_i(self):
#		print 'I am B'
	pass
class C:
	def who_am_i(self):
		print 'I am C'

class D(B,C):
#	def who_am_i(self):
#		print 'I am D'
	pass

d = D()
print d.who_am_i()
				
