number = int(input())
for i in range(number) :
    word = input()
    if len(word)<= 10 :
        print(word)
    else:    
        print(word[0]+str(len(word)-2)+word[len(word)-1])