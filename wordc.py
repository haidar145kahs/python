word = input()
if word[0].islower():
        cap= str(word[0].upper())
        print(cap + word[1:])
else:
    print(word)