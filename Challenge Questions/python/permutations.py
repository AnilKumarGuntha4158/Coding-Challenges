from itertools import permutations
str1="123"
str2=str1[::-1]
#str2=reversed(str1)
print(str2)
count=0
permlist=permutations(str1)
#print(list(permlist))
for perm in list(permlist):
	#print(perm)
	print(''.join(perm))
	count=count+1
print(count)
