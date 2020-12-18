def expression(x):
    for a,b,c, in x:
        print(a,b,c)

def U(x, repeat):
    p="U" if repeat == 1 else "U'"
    for _ in range(repeat):
        x[0].append(x[0].pop(0))
    return print(p), expression(x)    

def R(x, repeat):
    arr=[]
    p="R" if repeat == 1 else "R'"

    for _ in range(repeat):
        for i in range(3):
            arr.append(x[i].pop())
        arr.append(arr.pop(0))
        for i in range(3):
            x[i].append(arr.pop(0))
    return print(p),expression(x)

def L(x, repeat):
    arr=[]
    p="L" if repeat == 1 else "L'"
    for _ in range(repeat):
        for i in range(3):
            arr.append(x[i].pop(0))
        arr.insert(0,arr.pop())
        for i in range(3):
            x[i].insert(0,arr.pop(0))
    return print(p),expression(x)
    
def B(x,repeat):
    p="B" if repeat == 1 else "B'"
    for _ in range(repeat):
        x[2].insert(0, x[2].pop())
    return print(p),expression(x)
   
def matching_func(y,i,repeat):
    if y[i]=="U":
        U(x, repeat)
    elif y[i]=="R":
        R(x, repeat)
    elif y[i]=="L":
        L(x, repeat)
    elif y[i]=="B":
        B(x, repeat)


        

x= [['R', 'R', 'W'], ['G', 'C', 'W'], ['G', 'B', 'B']]
keepgoing=True

expression(x)

while True:
    y = input('CUBE>').upper()

    for i in range(len(y)):
        if (len(y)==1 and i==0) or (i==len(y)-1):
            if y[i]=='Q':
                print("Bye~")
                keepgoing=False
                break
            repeat=1
            matching_func(y,i,repeat)

        elif len(y)>1 and i<len(y)-1:
            if y[i]!="'" and y[i+1]!="'":
                repeat=1
                matching_func(y,i,repeat)
                
            elif y[i]!="'" and y[i+1]=="'":
                repeat=2
                matching_func(y,i,repeat)
    
    if keepgoing==False:
        break
    
