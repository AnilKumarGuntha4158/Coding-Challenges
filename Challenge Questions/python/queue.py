n=int(input())
k=int(input())
a=list()

for i in range(0,k):
    b=int(input())
    a.append(b)
p=int(input())
for i in range(0,p):
    a.remove(a[0]) 
print('len:',len(a))  
for i in range(0,len(a)):
    print(a[i],end=' ')
    
