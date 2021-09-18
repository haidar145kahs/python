l = list()
for i in range(5):
    t = input()
    for j in t.split(' '):
        l.append(int(j))
for i in range(len(l)):
    if l[i]!=0 :
        c = int(i%5) 
        r = int(i/5)
        x = int(abs(2-c))
        y = int(abs(2-r)) 
        print(x+y)  
