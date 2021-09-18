n = input()
l = [] 
for i in range(len(n)):
    if n[i]!= '+':
        l.append(n[i])
l.sort()
s = ''
for i in range(len(l)):
    if i < len(l)-1:
        s+=l[i] +"+"
    else:
        s+= l[i]
print(s)            