l=[]
new=[]
marks=[]
for i in xrange(input()):
    sub=[]
    sub.append(raw_input())
    sub.append(input())
    marks.append(sub[1])
    l.append(sub)
marks.sort()
ref=marks[0]
for val in marks:
    if val>ref:
        ref=val
        break
for i in l:
    if i[1]==ref:
        new.append(i[0])
new.sort()
for i in new:
    print i
    
