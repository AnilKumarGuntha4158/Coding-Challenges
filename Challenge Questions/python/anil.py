def swapcase(s1):
	str1=''
	#print(s1)
	for i in s1:
		ch=ord(i)
		if(ch>=65 and ch<=90):
			ch=ch+32
			str1=str1+chr(ch)
			continue
		if(ch>=97 and ch<=122):
			ch=ch-32
			str1=str1+chr(ch)
			continue
		else:
			str1=str1+chr(ch)
	return str1






s=input()
a=swapcase(s)
print(a)
