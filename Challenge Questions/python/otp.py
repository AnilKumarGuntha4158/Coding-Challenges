import math
a=input()
s=''
s1=''
for i in a:
	if(int(i)%2!=0):
		#print('i',i)
		s=int(math.pow(int(i),3))
		s1=s1+str(s)
		#print(s1)
		
if(len(s1)==4):
	print(int(s1))
else:
	print("Invalid Otp")

