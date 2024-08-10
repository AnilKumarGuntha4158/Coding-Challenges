n=int(input())
l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
l3=list(map(int,input().split(" ")))
#print(l1[2:5])
n1=int(input())
r4=[]
r5=[]
for i in range(0,n1):
	r1=[]
	r2=[]
	r3=[]
	qu=list(map(int,input().split(" ")))
	#print(qu)
	r1=l1[qu[0]-1:qu[1]].copy()
	r1.extend(l2[qu[2]-1:qu[3]].copy())
	r1.extend(l3[qu[4]-1:qu[5]].copy())
	#r1.extend(r2)
	#r1.extend(r3)
	r4=r1.copy()
	#print(set(r1))
	#print(len(set(r1)))
	r5.append(len(set(r1)))
for i in range(0,len(r5)-1):
	print(r5[i])
print(r5[len(r5)-1],end='')

	

	

		
