k = int(input())
string = input()
d = dict()
s =set()
arranged = ''
flag=False
if len(string)%k == 0 :
    for i in string:
        if i in s:
            d[i]+=1
        else:
            s.add(i)
            d[i]=1

    for i in s:
        if d[i]%k == 0 :
            for j in range(int(d[i]/k)):
                arranged+=i
        else:
            flag = True
            break
    if flag:
        print('-1')
    else:
        ans = ''
        for i in range(k):
            ans+=arranged
        print(ans)    
else:
    print('-1')
