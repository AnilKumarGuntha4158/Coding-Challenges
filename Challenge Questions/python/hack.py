k=int(input())
n=int(input())
a=[]
c1=0
for i in range(0,n):
	c=int(input())
	a.append(c)
m=max(a)
b=list(set(a))
#+a=sorted(a)
#d=a[1]
print(b)
print(a)
for i in range(1,len(b)-2):
	for j in range(1,n-1):
		if(a[i]>a[i-1] and  a[i]+k==m):
			c1=c1+1
			print('a:',a[i],end='')
print('c1',c1)
