i=0
n=int(input(""))
for z in range(0,n):
    s=input("")
    n,m,k=s.split()
    n=int(n)
    m=int(m)
    k=int(k)
    if n+k+m>1:
            i+=1
            
print(i)
