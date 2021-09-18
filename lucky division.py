array = []
v = ''
i = 0
while i < 7 :
    array.append(v+"4")
    array.append(v+"7")
    v = array[i]
    i+=1

n = int(input())
almost_lucky = False 
for i in array:
    if int(i) > n:
        break

    if n % int(i)==0:
        almost_lucky=True
        break
    
if almost_lucky:
    print('YES')
else:
    print('NO')