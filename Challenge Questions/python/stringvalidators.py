import sys
line = sys.stdin.readline()
truth = [False,False,False,False,False]
for i in line:
    if i.isalnum(): truth[0] = True
    if i.isalpha(): truth[1] = True
    if i.isdigit(): truth[2] = True
    if i.islower(): truth[3] = True
    if i.isupper(): truth[4] = True
        
for i in truth:
    print(i)
   
