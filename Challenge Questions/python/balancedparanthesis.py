def checkbalanced(s):
	openlist=['(','[','{']
	closelist=[')',']','}']
	stack=[]
	stack1=[]
	for i in s:
		if i in openlist:
			stack.append(i)
			#print(stack)
		elif(i in closelist):
			a=closelist.index(i)
			#print(a)
			if((len(stack)>0) and openlist[a]==stack[len(stack)-1]):
				stack.pop()
			else:
				return "unbalanced"
		
	if(len(stack)==0):
		return "balanced"

a=input()
c=checkbalanced(a)
print(c)
