a=int(input('enter number of students'))
c=0
d=[]
for  i in range (a):
    p=int(input('enter  point'))
    d.append(p)
    c=p+c
mx=max(d)
mn=min(d)
print('minimum point is',mn)
print('maximum point is',mx)
print('average is',c/a)