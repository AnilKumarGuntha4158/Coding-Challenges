if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=student_marks.get(query_name)
    sum1=0
    c=0
    for i in a:
        sum1=sum1+i
        c=c+1
    a=sum1/c
    print("%.2f" % a)
    print("%.2f" % a)
    #print("%.2f" % sum1/c,end=" ")

