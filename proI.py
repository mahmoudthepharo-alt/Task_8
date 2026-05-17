n=int(input(""))
z=0
for i in range(n):
    p,q=input("").split()
    p=int(p)
    q=int(q)
    if q-p>1:
        z+=1
print(z)