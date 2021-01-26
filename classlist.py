with open('10d.txt','r') as f:
    a=f.readline()
b=sorted(a)
with open('lcrescator.txt','w') as f:
    f.write(str(b))
a.sort(reverse=True)
with open('descrescator.txt','w') as f:
    f.write(str(a))