n,k = input().split(' ')
n = int(n)
k = int(k)
if n%2 != 0 :
    if k <= (n/2)+1:
        print((2*k)-1)
    else:
        print(((2*k)-n)-1)
else:
    if k <= (n/2):
        print((2*k)-1)
    else:
        print((2*k)-n)