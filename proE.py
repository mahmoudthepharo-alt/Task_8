n = int(input(""))
l=[]
for i in range(0,n):
    r=int(input(""))
    if r>=1900:
        l.append("Division 1")
    elif r>=1600:
       l.append("Division 2")
    elif r>=1400:
        l.append("Division 3")
    else:
        l.append("Division 4")
print(*l,sep="\n")