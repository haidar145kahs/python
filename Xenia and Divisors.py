input()
n = input().split(' ')
a = []
b = []
c = []
errorFlag = False
n.sort()
for i in n:
    if int(i)== 1:
        a.append(int(i))
    elif int(i)== 2 or int(i)== 3:
        b.append(int(i))
    elif int(i)== 4 or int(i)== 6:
        c.append(int(i))
    else:
        errorFlag = True
plist = list()
if len(a)==len(b)==len(c) and not errorFlag:
    for i in range(int(len(n)/3)) :
        if b[i]== 3 and c[i] == 4 :
            errorFlag = True
            break
        plist.append(str(a[i])+" "+str(b[i])+" "+str(c[i])+" ")
else:
    errorFlag = True
if errorFlag:
    print('-1')
else:
    for i in plist:
        print(i)