a=list(input())
print(a)
k=0
str1=""
r=len(a)-1
print(k,r)
while(k<r):
	print(a[k],a[r])
	if(not(a[k].isalpha())):
		k=k+1
		print(a[k])
	elif(not(a[r].isalpha())):
		r=r-1
		print(a[k])
	else:
		#print(a[k],a[r])
		t=a[k]
		a[k]=a[r]
		a[r]=t
		k=k+1
		r=r-1
b=str(a)
for i in a:
	str1=str1+i
print(str1)
