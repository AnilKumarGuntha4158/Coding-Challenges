def anil():
	a=list(map(int,input().split(" ")))
	r=[]
	if(a[0]<=1):
		return 0
	for i in range(1,len(a)):
		d=str(a[i])
		#print('d',d)
		l=[]
		if(len(d)==3):
			#print(d)
			for j in d:
				l.append(int(j))
			#print(l)
			mx=max(l)
			#print(mx)
			mn=min(l)
			#print(mn)
			r1=mx*11+mn*7
			#print(r1)
			r.append(r1)

	#print(r)
	rr=[]
	j=1
	#rr[0]=0
	for i in r:
		c1=str(i)
		if(len(c1)>2):
			s=c1[-2:]
			rr.insert(i,int(s))
			#print(j,int(s))
			j=j+1
		else:
			rr.insert(j,int(c1))
			#print(j,int(c1))
			j=j+1
	#print('rr',rr)
	#print('rr',rr)
	rra=[]
	for i in rr:
		rra.append(str(i))
	s=sorted(rr)
	s1=[]
	for i in s:
		s1.append(str(i))
	#print(s1)
	d1=s1[0][0]
	c1=0
	rrr=[]
	rr1=[]
	odd=[]
	even=[]

	odd1=[]
	even1=[]
	for i in range(0,len(rr)):
		#print('i',i)
		try:
			if((i+1)%2==0):
				#print('o',rr[i])
				odd1.append(rr[i])
			
			else:
				#print('e',rr[i])
				even1.append(rr[i])
		except IndexError:
			m='null'
	#print('even',even)
	even1=sorted(even1)
	odd1=sorted(odd1)
	#print(even1)
	#print(odd1)

	for i in even1:
		even.append(str(i))
		#print(str(i))
	for i in odd1:
		odd.append(str(i))
	#print('even',even)
	#print(odd1)

	for i in range(1,len(even)):
		if(d1==even[i][0]):
			c1=c1+1
			d1=even[i][0]
			continue
		else:
			rrr.append(c1)
			d1=even[i][0]
			c1=1
	rrr.append(c1)
	#print('a:',rrr)
	d=max(rrr)
	if(d%2==0):
		e1=d//2
	else:
		e1=d//2+1
	o1=d-e1
	result=o1*e1
	rrr=[]
	for i in range(0,len(odd)):
		if(d1==odd[i][0]):
			c1=c1+1
			d1=odd[i][0]
			continue
		else:
			#rr1.append(rra[i])
			rrr.append(c1)
			d1=odd[i][0]
			c1=1
	#print(rr1)
	rrr.append(c1)
	#print(rrr)
	d=max(rrr)
	#print('d2',d)
	if(d%2==0):
		e2=d//2
	else:
		e2=d//2+1
	o2=d-e2
	result=result+o2*e2
	return result
		
k=anil()
print(k)
	
	
	
		
