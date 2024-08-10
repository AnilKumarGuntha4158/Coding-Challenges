class student:
	def __init__(self,a,b,c):
		self.marks(a,b,c)
	def marks(self,a,b,c):
		self.a1=a
		self.b1=b
		self.c1=c
class anil(student):
	pass

s1=student(2,2,2)
print(s1.a1,s1.b1,s1.c1)
s2=anil(1,1,1)
#s2.marks(1,1,1)
print(s2.a1,s2.b1,s2.c1)
print(issubclass(anil,student))
print(issubclass(anil,object))
#every class is a sub class of an object that is happen implicitly
print(issubclass(student,object))

