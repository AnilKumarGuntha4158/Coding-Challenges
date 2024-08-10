n1=int(input())
l11=list(map(int,input().split(" ")))
l21=list(map(int,input().split(" ")))
l31=list(map(int,input().split(" ")))
#print(l1[2:5])
n12=int(input())
r11=[]
r21=[]
r31=[]
r41=[]
r51=[]
for i in range(0,n12):
	qu=list(map(int,input().split(" ")))
	#print(qu)
	r11=l1[qu[0]-1:qu[1]].copy()
	r11.extend(l2[qu[2]-1:qu[3]].copy())
	r11.extend(l3[qu[4]-1:qu[5]].copy())
	#r1.extend(r2)
	#r1.extend(r3)
	r41=r11.copy()
	#print(set(r1))
	#print(len(set(r1)))
	r51.append(len(set(r1)))
for i in range(0,len(r5)-1):
	print(r5[i])
print(r5[len(r5)-1],end='')

	

	

		
