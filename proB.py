l=[]
n=int(input(""))
for i in range(n):
    x=int(input(""))
    s = input()
    nums=s.split()
    z=[]
    y=[]
    for j in range(x):
        y.append(int(nums[j]))
        z.append(int(nums[j]))
        z.sort()
    if z[0] == z[1]:
        l.append(y.index(z[-1])+1)
    else:
        l.append(y.index(z[0])+1)
print(*l,sep="\n")