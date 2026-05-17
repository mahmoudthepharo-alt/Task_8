z=""
n=input("")
o=0
for i in range(0,len(n)):
    if o==1:
        o=0
        continue
    if n[i]==".":
        z+="0"
    elif n[i]=="-":
        if n[i+1]==".":
            z+="1"
        elif n[i+1]=="-":
            z+="2"
        o+=1

print(z)
