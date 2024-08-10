# Enter your code here. Read input from STDIN. Print output to STDOUT
def avi(k):
    if(k<9):
        return -1
    elif(k%10==9):
        return 1
    elif(k%9==0):
        return k//9
    elif(i==0):
        return 10
    else:
        if(avi(k-9)==-1):
           return -1
        else:
            return 1+avi(k-9)



n=int(input())
a=[]
c=[]
for i in range(0,n):
    b=int(input())
    a.append(b)
for i in a:
    if(i<9):
        c.append(-1)
    elif(i%10==9):
        c.append(1)
    elif(i%9==0):
        c.append(int(i/9))
    elif(i==0):
        c.append(10)
    else:
       d= avi(i)
       c.append(d)
for i in c:
    print(i)


