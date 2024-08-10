from itertools import permutations
a=list(map(str,input().split(" ")))
plist=permutations(a)
c=[]
for i in plist:
	a=' '.join(i)
	c.append(list(int(a,10)))
print(c)
	
	
