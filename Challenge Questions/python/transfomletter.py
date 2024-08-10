def swap_case(s):
    for i in s:
        ch=ord(i)
        print(ch)
        str=''
        if(ch>=65 and ch<=90):
            ch=ch+32
            print(ch)
            str=str+chr(ch)
        else:
            ch=ch-32
            print(ch)
            str=str-chr(ch)
    return str

if __name__ == '__main__':
    s = input()
    print(s.swapcase())
    result = swap_case(s)
    print(result)
