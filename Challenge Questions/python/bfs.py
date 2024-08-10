print("enter no of nodes:")
n=int(input())
mat=[]
for i in range(0,n):
	a=[]
	a=list(map(int,input().split(" ")))
	mat.append(a)
print(mat)
visited=[0]*n
#print(visited)
visited[0]=1
queue=[0]
node=queue.pop(0)
print(node)
while(True):
	for i in range(0,n):
		if(mat[node][i]==1 and visited[i]==0):
			visited[i]=1
			#print(i)
			queue.append(i)
	if(len(queue)==0):
		break
[	else:
		node=queue.pop(0)
		print(node)
		
