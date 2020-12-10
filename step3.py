
# TODO: 1.무작위 섞기 기능 추가 
#// TODO: 2.큐브를 완성했을 때 축하 메시지 띄우기
#// TODO: 3. B, D 함수 만들자
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
        

def matching_func(cube, y, i):
    if y[i] == "U":
        U(cube)
    if y[i] == "D":
        D(cube)
    if y[i] == "F":
        F(cube)
    if y[i] == "B":
        B(cube)
    if y[i] == "R":
        R(cube)
    if y[i] == "L":
        L(cube)


def checkResult(cube, start):
     
    if cube==perfect_cube:
        print("축하합니다😆\n큐브를 맞췄어요!!✨\n")
        quit(cube, start)
    else: 
        gameStart(cube, start)

def perform_order(cube,y):
    global count
    
    for i in range(len(y)): #!조건 구분 간결하게 정리하기.
        
        if len(y)==1 and y in alphabet:
            count+=1
            matching_func(cube, y,i)
            print(y[i])
            paintCube(cube, start)
        
                
        elif len(y)>1 and y[i] in alphabet and i<len(y)-1: #y+i가 존재하는 경우
            if y[i+1] in alphabet:
                count+=1
                matching_func(cube,y,i)
                print(y[i])
                paintCube(cube, start)
                    
            elif y[i+1]=="'":
                count+=1
                for _ in range(3):
                    matching_func(cube,y,i)
                print(y[i]+y[i+1])
                paintCube(cube, start)
                
            elif y[i+1]=="2":
                count+=1
                for _ in range(2):
                    matching_func(cube,y,i)
            
                print(y[i]+y[i+1])
                paintCube(cube, start)

        elif len(y)>1 and y[i] in alphabet and i==len(y)-1: #y[i]가 마지막 값, y+i가 없는 경우
            count+=1
            matching_func(cube, y,i)
            print(y[i])
            paintCube(cube, start)

    checkResult(cube, start)

        
def randomCube():
    print("will be ready")

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

import time

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

input_list=['F','R','U','B','L','D',"'","2","Q"]
alphabet=['F','R','U','B','L','D']
special=["'","2",""]
start=0
count=0

print("▶ 초기상태:") #초기 큐브 구현
paintCube(init_cube, start)

print("▶ Do you want Mixed Cube?")
mix=input("Enter Y or N:").upper()
start=time.time()

if mix == "Y":
    randomCube()
elif mix=="N":
    gameStart(init_cube,start)


