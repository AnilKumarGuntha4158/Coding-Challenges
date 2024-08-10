a=int(input())
b=[]
sum1=0
for i in range(1,a+1):
    c=int(input())
    b.append(c)
for l in range(1,len(b)+1):
    for k in range(1,len(b)+1-i):
        j=k+l-1
        d=[]
        for j in range(i,j+1):
            d.append(b[j])
            g1=sum(d)
        print(d)
        print(sum)
        if(sum1>g1):
            sum=g1
print(g1)
            
            
