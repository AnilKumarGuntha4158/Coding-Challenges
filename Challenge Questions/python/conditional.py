if __name__ == '__main__':
    N = int(input())
a2=[]
for i in range(0,N):
    a=list(map(str,input().split(" ")))
    #print(a)
    if(a[0]=='insert'):
        
        a2.insert(int(a[1]),int(a[2]))
        print(a2)
    if(a[0]=='append'):
        #n1=int(input())
        a2.append(int(a[1]))
    if(a[0]=='remove'):
        #n1=int(input())
        print(int(a[1]))
        a2.remove(int(a[1]))
        print(a2)
    if(a[0]=='sort'):
        a2.sort()
    if(a[0]=='pop'):
        a2.pop()   
    if(a[0]=='reverse'):
        a2.reverse()
    if(a[0]=='print'):
        print(a2)
