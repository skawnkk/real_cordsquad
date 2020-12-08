x= list(map(str,(input().split())))
print(x)

word=list(x[0])
move=int(x[1])
direction=x[2].upper()

if (direction=='L' and move>0) or (direction=="R" and move<0):
    move=abs(move)
    for i in range(move):
        word.append(word.pop(0))
    print("".join(word))

else:
    move=abs(move)
    for i in range(move):
        word.insert(0, word.pop())
    print("".join(word))
