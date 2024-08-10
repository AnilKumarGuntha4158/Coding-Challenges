def kmp(txt1,pat1):
	n=len(txt1)
	m=len(pat1)
	i=0
	j=0
	lp1=[0]*m
	a=pre(pat,m,lp1)
	#print(a)
	while(i<n):
		if(txt1[i]==pat1[j]):
			i=i+1
			j=j+1
			#print(j)
		if(j==m):
			print("the index is at",i-j)
			j=lp1[j-1]
		elif(i<n and pat1[j]!=txt1[i]):
			if(j!=0):
				j=lp1[j-1]
				#aprint(j)
			else:
				i=i+1
def pre(pat,m,lp):
	#print(lp)
	i=0
	j=1
	lp[0]
	while(j<m):
		if(pat[i]==pat[j]):
			i=i+1
			lp[j]=i
			j=j+1
		else:
			if(i!=0):
				i=lp[i-1]
			else:
				#lp[i]=0
				j=j+1
	#return lp
				
			
txt = input()
pat = input()
kmp(txt,pat)
