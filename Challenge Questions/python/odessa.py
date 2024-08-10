n=list(map(int,input().split(" ")))
print(n)
a=[]
for i in range(1,n[0]+1):
	a.append('00000')
for i in range(1,n[1]+1):
	t=[]
	t=list(map(int,input().split(" ")))
	if(t[0]==1):
		c=t[1]
		print('c:',c)
		c2=a[c-1]
		c1=int(a[c-1])
		print('c1:',c)
		d=t[2]
		if(c1==0):
			b=c2
			print('b:',b)
		else:
			b=bin(c1)[2:]
		#e=t[2]
		if(b[2]==0):
			a1=b[2]
			print('a1:',a1)
			a2=a[a1]
			print('a2:',a2)
			a[a1]=1
			d1=int(a[a1])
			print('d1:',d1)
			
		else:
			a1=b[2]
			a2=a[a1]
			a[a1]=0
			d1=int(a[a1])
			d1=int(a[a1])
			
		ad=int(b,2)
		a[d]=ad
			
		
print(a)
