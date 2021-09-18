a = []
b = []
c = []
ct = 0
n = int(input())
for i in range(n):
    at,bt = input().split(' ')
    a.append(at)
    b.append(bt)
for i in range(len(a)):
    ct=int(ct)-int(a[i])+int(b[i])
    c.append(ct)
print(max(c))   