tmp = ''
host = input()
guests = input()
both = input()
l_1 = list(host)
l_2 = list(guests)
l = l_1 + l_2
l_3 = list(both)
s_1 = set()
s_2 = set()
d_1 = dict()
d_2 = dict()
#for s_1 and d_1 : 
for i in l :
    if i in s_1:
        d_1[i]+=1
    else:
        s_1.add(i)
        d_1[i]=1
for i in l_3 :
    if i in s_2:
        d_2[i]+=1
    else:
        s_2.add(i)
        d_2[i]=1      
if d_1 == d_2:
    print('YES')
else:
    print('NO')    



#first try on this code 
#x = len(host)
#y = len(guests)
#a = x+y
#z = len(sum)
#if a == z :
#   print('YES')
#else:
    #print('NO')