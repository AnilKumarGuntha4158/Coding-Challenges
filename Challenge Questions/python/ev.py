a=input()
b=input()
c=len(a)
d=len(b)
i=0
j=0
s=''
while(i<c or j<d):
	if(i<c):
		s=s+a[i]
		i=i+1
	if(j<d):
		s=s+b[j]
		j=j+1
	if(i>c and j<d):
		s=s+b[j]
		j=j+1
	if(j>d and i<c):
		s=s+a[i]
		i=i+1
	
print(s)
	
