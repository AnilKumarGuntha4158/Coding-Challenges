def kmp(txt1,pat1):
	n=len(txt1)
	m=len(pat1)
	lps=[0]*m
	print(lps)
	j=0
	i=0
	computelps(pat1,m,lps)
	while(i<n):
		if(pat1[i]==txt1[j]):
			i=i+1
			j=j+1
		if(i==m):
			print("pattern is found at",j-i)
			i=lps[i-1]
		elif(j<n and pat1[i]!=txt1[j]):
			if(i!=0):
				i=lps[i-1]
			else:
				#lps[i]=0
				j=j+1
			
			
	
def computelps(pat,m1,lps):
	i=1
	l=0
	lps[0]=0
	print('anil')
	while(i<m1):
		#print('anil')
		if(pat[i]==pat[l]):
			print(pat[i])
			l=l+1
			lps[i]=l
			i=i+1
		else:
			print('anil3')
			if(l!=0):
				l=lps[i-1]
			else:
				lps[i]=0
				i=i+1
	print(lps)








txt=input()
pat=input()
kmp(txt,pat)
