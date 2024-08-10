n=int(input())
a=input() 
d=[]
for i in a:
    d.append(int(i))
    
d1=d.copy()
k=set(d)
k=list(k)
id1=[]
for i in d:
    if(d.count(i)%2==0):
        continue
    else:
        id2=d.index(i)
        id1.append(id2)
        id3=d1.index(i)
        d1.pop(id3)
#print(id1)
print(max(id1)-min(id1))
#print(d1)
