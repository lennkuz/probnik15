a=open('17-418.txt').readlines()
a=[int(x) for x in a]
def c6(n):
    r=''
    while n>0:
        r=str(n%6)+r
        n//=6
    return r
def c9(n):
    r=''
    while n>0:
        r=str(n%9)+r
        n//=9
    return r
mns6=10**20
for x in a:
    if len(c6(x))==4:mns6=min(x, mns6)

mns9=10**20
for x in a:
    if len(c9(x))==3:mns9=min(x, mns9)

k=0
s=[]
for i in range(len(a)-1):
    if len([int(x) for x in a[i:i+2] if x%11==mns6%5])>=1:
        if len([int(x) for x in a[i:i + 2] if x % 7 == mns9 % 13]) >= 1:
            k+=1
            s.append(sum(a[i:i+2]))
print(k,max(s))