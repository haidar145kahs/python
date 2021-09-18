word = input()
b = 0
s = 0 
for i in range(len(word)):
    if word[i].isupper():
        b += 1
    else:
        s+=1
if b>s :
    print(word.upper())
else:
    print(word.lower())    