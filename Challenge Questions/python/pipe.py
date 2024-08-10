n=int(input())
l=int(input())
#m=int(input())
a=[]
b=[]
c=[]
k=0
for i in range(0,l):
	d=int(input())
	a.append(d)
print(a)
m=[]
for i in a:
	if(i<=l):
		b.append(i)
	elif(i>l):
		
		c.append(b)
		c.append(m)
		b=[]
		b.append(i)
		m=[]
c.append(b)
print(c)
g=[]
for i in c:
	if(len(i)==0):
		continue
	else:
		g.append(i)
print(g)
m=0
for i in g:
	m=m+min(i)
print(m)
'''
for i in c:
	m=min(i)
	k=k+m
print(k)'''
	
