n = int(input(""))
p = []
for i in range(0,n):
    n,t,s=input("").split()
    l = [int(n),int(t),int(s)]
    l.sort()
    if l[0] + l[1] == l[2]:
        p.append("YES")
    else:
        p.append("NO")
print(*p,sep="\n")