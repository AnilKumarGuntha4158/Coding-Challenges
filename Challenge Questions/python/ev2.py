a=list(map(int,input().split(" ")))
a.sort()
b=[]
j=0
if(len(a)%2==0):
	for i in range(0,int(len(a)/2)):
		b.append(a[i])
		b.append(a[len(a)-1-i])
#print(b)
else:
	for i in range(0,int(len(a)/2)+1):
		b.append(a[i])
		b.append(a[len(a)-1-i])
for i in range(0,len(b)-1):
	print(b[i],end=" ")
	
