x = 0 
y=0
z=0
n=int(input())

for i in range(n):
    xt,yt,zt = input().split(' ')
    x+=int(xt)
    y+=int(yt)
    z+=int(zt)

if x==y==z==0: 
    print('YES')
else:
    print('NO')


