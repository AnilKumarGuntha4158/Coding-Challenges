d1={'anil':4152}
n=int(input())
for i in range(0,n):
	a=input()
	b=int(input())
	d2={a:b}
	d1.update(d2)
print(d1)
c=list(d1.values())
f=list(d1.keys())
print(c)
d=sorted(c,reverse=True)
print(d)
c=d[1]
newdict = {1:0, 2:0, 3:0}
a=list(d1.keys())
print(a)
for i in a:
	if(c==d1.get(i)):
		print(i)
