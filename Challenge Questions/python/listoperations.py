'''a=[]
b=[]
print("enter length")
n=int(input())
for i in range(1,n+1):
	c=int(input())
	a.append(c)
	b.append(c)
print(a)
print(len(a))
print(min(a))
print(max(a))
d=a.copy()
print("copied list:",d)
print(sum(a))
d.sort()
print(d)
d.sort(reverse=True)
print(d)'''
d={}
for i in range(3):
	k=input("enter key")
	v=input("enter value")
	d1={k:v}
	d.update(d1)
print(d)




	
