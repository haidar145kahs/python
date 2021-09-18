n,m = input().split(' ')
n =int(n)
m =int(m)
tasks = input().split(' ')
a = []

ans = 0
#to get the input in intiger :
for i in tasks:
    a.append(int(i))
#_______________________
pos = 1
for i in range(m):
    if a[i] > pos:
        ans += a[i]-pos 
    elif a[i]< pos :
        ans+= n - pos + a[i]
    pos = a[i] 
print(ans)   
