''' 
< 0 >
B B B  
B B B
B B B

< 1 >     < 2 >     < 3 >     < 4 >
W W W     O O O     G G G     Y Y Y 
W W W     O O O     G G G     Y Y Y 
W W W     O O O     G G G     Y Y Y 
 
< 5 >
R R R 
R R R 
R R R 
'''
def linkedFace(cube,index):
    target = cube[index][0][0]
    cube[index][0][0] = cube[index][2][0]
    cube[index][1][0] = cube[index][2][1]
    cube[index][1][2] = cube[index][0][1]
    cube[index][2][0] = cube[index][2][2]
    cube[index][2][1] = cube[index][1][2]
    cube[index][2][2] = cube[index][0][2]
    cube[index][0][1] = cube[index][1][0]        
    cube[index][0][2] = target

def U(cube):
    target = cube[1][0] 
    cube[1][0] = cube[2][0]
    cube[2][0] = cube[3][0]
    cube[3][0] = cube[4][0]
    cube[4][0] = target
    linkedFace(cube, 0)

def D(cube):
    target = cube[1][2]
    cube[1][2] = cube[4][2]
    cube[4][2] = cube[3][2]
    cube[3][2] = cube[2][2]
    cube[2][2] = target
    linkedFace(cube, 5)

def F(cube):
    target = cube[0][2]
    cube[0][2] = [cube[4][2][2], cube[4][1][2], cube[4][0][2]]
    cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[5][0]
    cube[5][0] = [cube[2][2][0], cube[2][1][0], cube[2][0][0]]
    cube[2][0][0], cube[2][1][0], cube[2][2][0]  = target
    linkedFace(cube, 1)

def B(cube):
    target = cube[0][0]
    cube[0][0] = [cube[2][0][2], cube[2][1][2], cube[2][2][2]]
    cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
    cube[5][2][0], cube[5][2][1], cube[5][2][2] = cube[4][0][0], cube[4][1][0], cube[4][2][0]
    cube[4][0][0], cube[4][1][0], cube[4][2][0] = target
    linkedFace(cube, 3)

def R(cube):
    target = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
    cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
    cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
    cube[3][0][0], cube[3][1][0], cube[3][2][0] = cube[0][2][2], cube[0][1][2], cube[0][0][2]
    cube[0][0][2], cube[0][1][2], cube[0][2][2] = target
    linkedFace(cube, 2)

def L(cube):
    target = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
    cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[0][0][0], cube[0][1][0], cube[0][2][0]
    cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
    cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
    cube[5][2][0], cube[5][1][0], cube[5][0][0] = target
    linkedFace(cube, 4)
        
def matching_func(cube, z):
    if z[0] == "U":
        U(cube)
    if z[0] == "D":
        D(cube)
    if z[0] == "F":
        F(cube)
    if z[0] == "B":
        B(cube)
    if z[0] == "R":
        R(cube)
    if z[0] == "L":
        L(cube)

def checkResult(cube, start):
    if cube==perfect_cube:
        print("축하합니다😆\n큐브를 맞췄어요!!✨\n")
        quit(cube, start)
    else: 
        gameStart(cube, start)

def perform_order(cube,y):
    global count  
    z=list(y)
    for i in range(len(z)):
        if z[i] not in orderlist:
            print("typing_Error")
            gameStart(cube, start)
            return
        
    while z:
        if len(z)==1:
            if z[0] in alphabet:
                count+=1
                print(z[0])
                matching_func(cube, z[0])
                paintCube(cube, start)
                z.pop(0)
            else:
                print("Typing_ERROR:", z[0])
                gameStart(cube, start)

        elif len(z)>1:
            if z[0] in alphabet and z[1] in alphabet:
                count+=1
                print(z[0])
                matching_func(cube, z[0])
                paintCube(cube, start)
                z.pop(0)

            elif z[0] in alphabet and z[1]=="'":
                count+=1
                print(z[0]+z[1])
                for _ in range(3):
                    matching_func(cube,z[0]+z[1])
                paintCube(cube, start)
                for _ in range(2):
                    z.pop(0)  

            elif z[0] in alphabet and z[1]=="2":
                count+=1
                print(z[0]+z[1])
                for _ in range(2):
                    matching_func(cube, z[0]+z[1])
                paintCube(cube, start)
                for _ in range(2):
                    z.pop(0)
                
            elif z[0] not in alphabet:
                print("Typing_ERROR:",z[0])
                gameStart(cube, start)
    checkResult(cube, start)

def perform_random_order(cube,y):
    z=list(y)
    while z:
        if len(z)==1 and z[0] in alphabet:
            matching_func(cube, z[0])
            z.pop(0)
             
        elif len(z)>1:
            if z[0] in alphabet and z[1] in alphabet:
                matching_func(cube, z[0])
                z.pop(0)

            elif z[0] in alphabet and z[1]=="'":
                for _ in range(3):
                    matching_func(cube,z[0]+z[1])
                for _ in range(2):
                    z.pop(0)
    
            elif z[0] in alphabet and z[1]=="2":
                for _ in range(2):
                    matching_func(cube, z[0]+z[1])
                for _ in range(2):
                    z.pop(0)

    paintCube(cube, start)
    gameStart(cube, start)
        
def randomCube():
    arr=[]
    for _ in range(len(alphabet)):
        alphabet_random = random.sample(alphabet,1)
        special_random = random.sample(special,1)
        arr.append(''.join(alphabet_random+special_random))
    random_order=''.join(arr)
    print("▶Mixed Cube:")
    # print(random_order)
    perform_random_order(init_cube, random_order)

def quit(cube, start):
    end=time.time()
    interval = time.localtime(end-start)
    print("경과시간:", time.strftime('%M:%S', interval))
    print("조작갯수:", count)
    print("이용해주셔서 감사합니다. 뚜뚜뚜.")

def gameStart(cube, start):
    y = input('CUBE>').upper()
    if y=="Q":
        quit(cube, start)
        return
    else:
        perform_order(cube, y)    

def paintCube(cube, start):
    for i in range(3):  
        for j in range(3):
            print(cube[0][i][j], end="")
        print("")
    print()

    for t in range(3):
            for i in range(1,5):
                for j in range(3):
                    print(cube[i][t][j], end="")
                print("   ", end="")
            print()
    print()

    for i in range(3):
        for j in range(3):
            print(cube[5][i][j], end="")
        print()
    print()

    
# --조건 및 입력 받는 부분----------------------------------------------------")

import time, random

color='BWOGYR'

# 초기큐브
init_cube = [[[] for _ in range(3)] for _ in range(6)]
for j in range(3):
    for i in range(6):
        for _ in range(3):
            init_cube[i][j].append(color[i])   

# 완성큐브
perfect_cube = [[[] for _ in range(3)] for _ in range(6)]
for j in range(3):
    for i in range(6):
        for _ in range(3):
            perfect_cube[i][j].append(color[i])    

orderlist=['F','R','U','B','L','D',"'","2","Q"]
alphabet=['F','R','U','B','L','D']
special=["'","2",""]
start=0
count=0

print("▶ 초기상태:")
paintCube(init_cube, start)

print("▶ Do you want Mixed Cube?")
mix=input("Enter Y or N:").upper()
start=time.time()

if mix == "Y":
    randomCube()
elif mix=="N":
    gameStart(init_cube,start)


