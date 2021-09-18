prog = input()
tmp = ''
for i in range(len(prog)):
    if prog[i]=='Q'or prog[i]=='H'or prog[i]=='9':
            tmp = 'YES'
            #print(tmp)
            break
    else:
        tmp = 'NO' 
        break 
        #print(tmp)       
print(tmp)        