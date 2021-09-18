#finding the most frequnt element in list : 
from typing import Counter
def most_frequnt(list):
    counter = 0
    num = list[0]
    
    for i in list : 
        f = list.count(i)
        if(f > counter):
            counter = f 
            num = i 
    return num 
# ____________________________________
n = int(input())
m = []
temp = 0
for i in range(n) :
    line=input()
    m.append(line)
print(most_frequnt(m))