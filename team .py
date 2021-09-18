n = int(input())
pages = input().split(' ')
tmp = 0
c = 0 
while tmp < n :
    for i in range(len(pages)):
        if tmp < n : 
            tmp+=int(pages[i])
            c= i
        else :
            break
print(c+1)