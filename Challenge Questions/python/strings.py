n=int(input())
a=[]
v=['a','e','i','o','u','A','E','I','O','U']

for i in range(0,n):
	c=input()
	a.append(c)
for i in range(0,len(a)):
	if(i==0):
		for j in a[i]:
			if j in v:
				print('"',end='')
			else:
				print(j,end='')
		print(end='\n')
	if(i==1):
		for j in a[i]:
			if j in v:
				print(j,end='')
			else:
				print('*',end='')
		print(end='\n')
	if(i==2):
		for j in a[i]:
			j=ord(j)
			if(j>=97 and j<=122):
				j=chr(j-32)
				print(j,end='')
			elif(j==" "):
				print(j,end='')
			else:
				print(chr(j),end='')
		
			
			
