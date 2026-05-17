n = int(input(""))
l=[]
z=0
for i in range(0,n):
    x = int(input(""))
    names=input("")
    s,t=names.split()
    for a in range(0,x):      
        if s[a] in t:

            t=t.replace(s[a], "",1)
        else:
            z=1
            break
    
    if z==0:
        l.append("YES")
    else:
        l.append("NO")
        z=0
print(*l,sep="\n")