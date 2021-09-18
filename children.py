n,m = input().split(' ')
a = input().split(' ')
MAX = 0
ind = 0
#big = max(a)
#ind = a.index(big)
for i in range(len(a)):
    tmp = int(int(a[i])/int(m))
    if int(a[i]) % int(m)!=0:
        tmp+=1
    #print("i: ",tmp)
    if tmp >= MAX:
        MAX =  tmp 
        ind = i  
print(ind+1)  