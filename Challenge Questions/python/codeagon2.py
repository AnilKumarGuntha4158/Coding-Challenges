n=int(input())
a=[]
c=0
f=0
for i in range(0,n):
	b=int(input())
	a.append(b)
for i in a:
	
	while(i>=9):
		if(i%10==9):
			f=1
			break
		else:
			i=i-9
			c=c+1
	if(f==1):
		c=c+1
	else:
		c=-1
		
	print(c)
	c=0
	f=0
		
	
		
