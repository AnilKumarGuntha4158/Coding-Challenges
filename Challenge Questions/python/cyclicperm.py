n=int(input())
a=[]
for i in range(0,n):
	c=input()
	a.append(c)
b=list(set(a))
d=list(a[0])
c=0
k=len(b)
s1=1
m=[]
for i in d:
	s=''
	v=d.pop(0)
	d.append(v)
	s=''.join(d)
	print(s)
	m.append(s)
	print(m)
m1=m[0]
for i in m:
	if(i in b):
		b.pop(i)
		if(len(b)==0):
			break
	else:
		c=c+1
		print(c)
	



	
	
	'''
	for j in range(0,len(b)):
		print(len(b))
		if(s==b[j]):
			print('s:',s)
			print('s1:',b[j])
			
			b.pop(j)
			s1=j
			print(b)
			if(len(b)==0):
				break
		else:
			c=c+1
			print(c)
	if(len(b)==0):
		break'''
print(c)
	
			
	
