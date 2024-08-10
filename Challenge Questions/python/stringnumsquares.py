import math
a=input()
sum1=0
for i in a:
	if(i.isdigit()):
		sum1=sum1+math.pow(int(i),2)
print(sum1)
		
