n = int(input())
x = 0
tmp = 0 
for i in range(n):
    m = input()
    if m == 'X++'or m == '++X':
        x+=1 
    if m == 'X--'or m== '--X':
        x-=1
print(x)