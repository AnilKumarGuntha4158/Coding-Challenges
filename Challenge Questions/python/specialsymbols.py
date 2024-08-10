a=input()
c=0
d=[]
for i in a:
	if(not(i.isalnum())):
		c=c+1
	if(i.isdigit()):
		d.append(int(i))
		
print(c)
print(d)
