k = int(input())
string = input()
d = dict()
s =set()
for i in string:
    if i in s:
        d[i]+=1
    else:
        s.add(i)
        d[i]=1
print(s)
print(d)