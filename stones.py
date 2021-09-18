n = int(input())
colour = input()
count = 0 
for i in range(len(colour)-1):
    if colour[i]== colour[i+1]:
        count+=1  
    else:
        continue  
print(count)