from itertools import combinations
a=list(map(int,input().split(" ")))
b=[]
for i in range(1,a[1]+1):
	b.append(i)
if(a[1]%a[0]!=0):
	d=list(combinations(a[0],a[0]))
	print(len(d))
else:
	d=list(combinations(a[1],a[0]))
	print(len(d))
