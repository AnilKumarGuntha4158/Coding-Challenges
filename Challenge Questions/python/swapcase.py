def swap_case(s):
	str1=''
    for i in s:
        ch=ord(i)
        print(ch)
        str1=''
        if(ch>=65 and ch<=90):
            ch=ch+32
            print(ch)
            str1=str1+chr(ch)
        elif(ch>=97 and ch<=122):
            ch=ch-32
            print(ch)
            str1=str1+chr(ch)
            
    return str1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
