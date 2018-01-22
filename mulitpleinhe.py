class A:
	def test(self):
		print 'Class A'
class B:
	def test(self):
		print 'Class B'

class C(B,A):
	pass

c = C()
c.test()
c.test()
