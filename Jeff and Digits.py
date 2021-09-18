n = int(input())
numbers = input().split(' ')
numbers.sort(reverse=True)
s = ''
d = dict()
d['0'] = 0
d['5'] = 0
ans = ''
#to get the number in one insaperated line :        
for i in numbers:
    if n <=len(numbers):
        s += i         
for i in numbers :
    d[i]+=1 
extra = d['5']%9
if  d['5']>=9:
    d['5'] -= extra
    for i in range(d['5']):
        ans += '5'
    for i in range(d['0']):
        ans += '0'
else:
    ans ='0'
if not d['0']:
    ans = '-1'  
print(ans)