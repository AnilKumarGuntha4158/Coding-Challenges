import math
t=int(input())
q=0
z=1
for i in range(1,t+1):
	b=[]
	l=int(input())
	for j in range(1,l+1):
		a=[]
		a=list(map(int,input().split(" ")))
		#print(a)
		b.append(a)
#print('b:',b)
	c=[]
	d=[]
	e=[]
	for i in range(0,len(b)):
		c=[]
		count=0
		for j in range(0,len(b)):
			if(i!=j):
			#print(b[i],b[j])
				dist=math.sqrt(pow(b[i][0]-b[j][0],2)+pow(b[i][1]-b[j][1],2))
				c.append(dist)
			#print(dist)
		#print('c:',c)
		d.append(min(c))
		a=min(c)
		print("%.2f" % a,end=" ")
		for k in range(0,len(c)):
			if(c[k]<=2*a):
				count=count+1
		print(count)
		
			

		
		

		
