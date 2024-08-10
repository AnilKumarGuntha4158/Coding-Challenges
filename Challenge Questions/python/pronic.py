import math
def pronic(a):
	s=[]
	for i in a:
		d=int(math.sqrt(i))
		#print(d)
		#print(type(d))
		#print('i:',i)
		if(int(d*(d+1))==i):
			s.append(i)
	return s			
a=input()
n=len(a)
d=[]
for l in range(1,n+1):
	for i in range(0,n-l+1):
		j=i+l-1
		str1=""
		for k in range(i,j+1):
			#print(k)
			str1=str1+a[k]
		d.append(int(str1))
v=pronic(d)
print(list(set(v)))
	
