a={4158:2,4152:3,4203:4}
k=int(input())
v=int(input())
a.update({k:v})
print(a)
#del a['anil']
print(a)
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))
print('keys:',a.keys())
print(sorted(a))
print('values:',a.values())
#print(reversed(a))
d=dict(zip(['a','b','c'],[1,2,3]))
print(d)
print('len:',len(d))
a1=max(d.values())
print(a1)
a2=min(d.values())
print(a2)
a[a2]='anil'
print(a[a2])
print(a)

