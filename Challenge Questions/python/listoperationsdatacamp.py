''' list operations '''
a=list()
a1=[]
print(type(a))
print(type(a1))
print("enter n value:")
n=int(input())
for i in range(1,n+1):
	in1=int(input())
	a.append(in1)
print('a:',a)
a1.append("anil")
a1.extend(a)
print('a1:',a1)
a1.insert(1,'vinay')
b1=a1.copy()
print('b1:',b1)
for i in b1:
	print(b1.count(i))
print('bb1:',b1)
print(b1.pop(0))
print(b1.remove('vinay'))
print('ab1:',b1)
b1.sort()
print(b1)
b1.sort(reverse=True)
sorted(b1,reverse=True)
print(b1)
b1.clear()
print(b1)

