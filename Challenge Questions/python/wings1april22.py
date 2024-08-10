from itertools import combinations_with_replacement
s=input()
s1=list(input())
n=''
for i in s:
	if(i in s1):
		n=n+i
print(n)
c=list(combinations_with_replacement(s1,len(n)))
print(c)
a=[]
for i in c:
	a.append("".join(i))
print(a)
b1=[]
for i in a:
	if(i==n):
		b1.append(i)
print(b1)
		
'''	
a=[]
for i in c:
	if(str(i)=="HS")):
		a.append(i)
print(a)'''
		
