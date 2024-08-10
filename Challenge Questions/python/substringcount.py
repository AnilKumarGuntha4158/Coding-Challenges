def count_substring(string, sub_string):
    count=0
    for i in range(0,len(string)):
        a=[]
        for j in range(i,len(string)):
            
            a.append(string[j])
            print(a)
            s1=''.join(a)
            if(s1==sub_string):
                count=count+1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
