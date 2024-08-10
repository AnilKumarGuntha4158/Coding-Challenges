a=input()
c=[]
c1=[]
for i in a:
	if(i.isdigit()):
		c.append(i)
	if(i.isalpha()):
		c1.append(i)
if(c==len(c1)):
	print("True",end=' ')
	print(len(c1))
else:
	print("False",end=' ')
	print(len(c1))
		
