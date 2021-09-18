def summer(n):
    sum = 0
    for i in n :
        sum+=int(i)
    return sum 

n = input()
count = 0
tmp = n
while len(tmp) > 1:
    tmp = str(summer(tmp))
    count+=1
    
print(count)