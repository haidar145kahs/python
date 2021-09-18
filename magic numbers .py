n = input()
temp ="YES"
right = 0
left = 0
holding = 0
n = n[::-1]
l = len(n)
while right < l :
    holding = right-left+1
    if  holding==1:
        if n[right]== '1':
            right+=1
            left = right
        else:
            right+=1   
    elif holding==2 :
        
        if n[left:right+1]=='41':
            right+=1
            left = right
        else:
            right+=1
    elif holding== 3:

        if n[left:right+1]=="441":
            right+=1
            left = right
        else:
            
            temp='NO'
            break
if(right-left != 0):
    temp="NO"
print(temp)    