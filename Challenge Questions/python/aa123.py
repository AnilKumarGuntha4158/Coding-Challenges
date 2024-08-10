n=int(input())
a=0
b=1
print(a,end='')
print(b,end='')
c=a+b
while(c<n):
	print(c,end=' ')
	a=b
	b=c
	c=a+b
	

	
