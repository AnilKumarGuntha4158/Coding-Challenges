from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
l=permutations("ABCD")
for i in l:
	print("".join(i))
print("")
l1=combinations(['A','B','C','D'],2)
for i in l1:
	print("".join(i))
l1=combinations_with_replacement(['A','B','C','D'],2)
for i in l1:
	print("".join(i))


