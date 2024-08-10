n=int(input())
s=[]
s1=[]
for i in range(0,n):
	sa=input()
	saa=set(sa)
	#print(saa)
	if(len(saa)==26):
		s.append(sa)
	sb=input()
	if(len(sb)<=100):
		s1.append(sb)
#print(s)
#print(s1)
l1=[]
i=0
m=[]
for i in range(0,len(s)):
	st=""
	for j in s[i]:
		for k in s1[i]:
			if(j==k):
				st=st+k
	m.append(st)
for i in range(0,len(m)-1):
	print(m[i])
print(m[len(m)-1],end='')
	
			
