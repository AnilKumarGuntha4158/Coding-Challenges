# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(0,n+1):
    a=list(map(int,input().split(" ")))
    b=list(map(int,input().split(" ")))
    d=b.copy()
    f=[]
    v=1
    while(True):
        for i in d:
            if(i%a[1]==0):
                f.append(i//a[1])
        if(len(f)==len(d)):
            d=f.copy()
            f=[]
        else:
            break
    print(d)
    m1=min(d)
    m3=m1
    f1=0
    #d.remove(m1)
    m2=max(d)
    if((m1*a[1])<=m2):
        m1=m1*a[1]
        d.append(m1)
        f1=1
        d.remove(m3)
    m1=max(d)
    m2=min(d)
    print(m1-m2)
	
	
   
		
    
    
