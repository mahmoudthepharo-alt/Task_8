n=int(input(""))
l = []
for i in range(n):
    word = input("")
    if len(word) <11:
        l.append(word)
    else:
        l.append(word[0]+str(len(word)-2)+word[-1])
print(*l,sep="\n")