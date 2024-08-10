def lucky(n):
	l=2
	if(l>n):
		return 0
	if(n%l==0):
		return 1
	n=n-int(n/l)
	l=l+1
	return lucky(n)
l=2
n=int(input())
if(lucky(n)):
	print("given no is a lucky no")
else:
	print("given no is not a lucky no")
