def one(n,c1):
	for i in range(n+1,100001):
		v=list(bin(i)[2:])
		c=v.count('1')
		if(c==c1):
			return i
a=int(input())
l=[]
for i in range(0,a):
    n=int(input())
    l.append(n)
for i in l:
    v=list(bin(i)[2:])
    print(v)
    c=0
    c=v.count('1')
    k= one(i,c)
    print(k)
