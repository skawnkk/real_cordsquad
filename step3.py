'''
< 0 >
B B B  
B B B
B B B

< 1 >      < 2 >     < 3 >     < 4 >
W W W     O O O     G G G     Y Y Y 
W W W     O O O     G G G     Y Y Y 
W W W     O O O     G G G     Y Y Y 
 
< 5 >
R R R 
R R R 
R R R 
'''
# -초기 큐브 및 큐브구현 함수----------------------------------------------------

cube = [[] for _ in range(6)]
for _ in range(3):
    cube[0].append(['B','B','B'])    
    cube[1].append(['W','W','W'])
    cube[2].append(['O','O','O'])
    cube[3].append(['G','G','G'])
    cube[4].append(['Y','Y','Y'])
    cube[5].append(['R','R','R'])



def paintCube(cube):

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


# -입력함수처리 및 동작함수----------------------------------------------------


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
    
 
def U(cube,repeat):
    target = cube[1][0] 
    cube[1][0] = cube[2][0]
    cube[2][0] = cube[3][0]
    cube[3][0] = cube[4][0]
    cube[4][0] = target
    linkedFace(cube, 0)

def F(cube, repeat):
    target=cube[0][2]
    cube[0][2] = [cube[4][2][2], cube[4][1][2], cube[4][0][2]]
    cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[5][0]
    cube[5][0] = [cube[2][2][0], cube[2][1][0], cube[2][0][0]]
    cube[2][0][0], cube[2][1][0], cube[2][2][0]  = target
    linkedFace(cube, 1)

def R(cube, repeat):
    target = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
    cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
    cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
    cube[3][0][0], cube[3][1][0], cube[3][2][0] = cube[0][2][2], cube[0][1][2], cube[0][0][2]
    cube[0][0][2], cube[0][1][2], cube[0][2][2] = target
    linkedFace(cube, 2)

def L(cube, repeat):
    target = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
    cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[0][0][0], cube[0][1][0], cube[0][2][0]
    cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
    cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
    cube[5][2][0], cube[5][1][0], cube[5][0][0] = target
    linkedFace(cube, 4)
        

def matching_func(cube, y, i, repeat):
    for _ in range(repeat):
        if y[i] == "U":
            U(cube, repeat)
        if y[i] == "F":
            F(cube, repeat)
        if y[i] == "R":
            R(cube, repeat)
        if y[i] == "L":
            L(cube, repeat)

def perform_order(cube,y):
    
    for i in range(len(y)):
        repeat=1
        if (len(y)==1 and i==0) or (i==len(y)-1):
            matching_func(cube, y,i,repeat)

        elif len(y)>1 and i<len(y)-1:
            if y[i] in alphabet and y[i+1] in alphabet:
                matching_func(cube,y,i,repeat)
                    
            elif y[i] in alphabet and y[i+1]=="'":
                repeat=3
                matching_func(cube,y,i,repeat)

            elif y[i] in alphabet and y[i+1]=="2":
                repeat=2
                matching_func(cube,y,i,repeat)
    paintCube(cube)
  

# --조건 및 입력 받는 부분----------------------------------------------------")

order=['F','R','U','B','L','D',"'","2"]
alphabet=['F','R','U','B','L','D']

keepgoing=True
paintCube(cube)
count=0

while True:
    y = input('CUBE>').upper()
    for i in y:
        if i not in order:
            print('typing_error!')
            keepgoing=False
            break
        elif i=='Q':
            print("경과시간:")
            print("조작갯수:")
            print("이용해주셔서 감사합니다. 뚜뚜뚜.")
            keepgoing=False
            break
    if keepgoing==False:
        break
    perform_order(cube,y)

# -루빅큐브 초기상태 평면도 구현---------------------------------------------

