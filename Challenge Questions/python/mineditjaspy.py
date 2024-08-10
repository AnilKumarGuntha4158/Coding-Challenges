a=input()
b=len(a)
l=b//2
c1=0
c2=0
c3=0
m=0
print(b,l)

for i in range(0,l):
	if(ord(a[i])>ord(a[l+i])):
		print(a[i],a[l+i],'c1:',c)
		c1=c1+1
	elif(ord(a[i])==ord(a[l+i])):
		c2=c2+1
	else:
		c3=c3+1
if(c1>c2 and c1>c3):
	m=c1
elif(c2>c1 and c2>c3):
	m=c2
else:
	m=c3
print(l-m)
