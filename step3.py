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

def U(cube):
    target = cube[1][0] 
    cube[1][0] = cube[2][0]
    cube[2][0] = cube[3][0]
    cube[3][0] = cube[4][0]
    cube[4][0] = target
    linkedFace(cube, 0)

def F(cube):
    target=cube[0][2]
    cube[0][2] = [cube[4][2][2], cube[4][1][2], cube[4][0][2]]
    cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[5][0]
    cube[5][0] = [cube[2][2][0], cube[2][1][0], cube[2][0][0]]
    cube[2][0][0], cube[2][1][0], cube[2][2][0]  = target
    linkedFace(cube, 1)

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
    if y[i] == "F":
        F(cube)
    if y[i] == "R":
        R(cube)
    if y[i] == "L":
        L(cube)

def perform_order(cube,y):
    global count
    
    for i in range(len(y)):
        
        if (len(y)==1 and i==0) or (y[i] in alphabet and i==len(y)-1):
            count+=1
            matching_func(cube, y,i)
            print(y[i])
            paintCube(cube)
           
        elif len(y)>1 and i<len(y)-1:
            if y[i] in alphabet and y[i+1] in alphabet:
                count+=1
                matching_func(cube,y,i)
                print(y[i])
                paintCube(cube)
                    
            elif y[i] in alphabet and y[i+1]=="'":
                count+=1
                for _ in range(3):
                    matching_func(cube,y,i)
                print(y[i]+y[i+1])
                paintCube(cube)

            elif y[i] in alphabet and y[i+1]=="2":
                count+=1
                for _ in range(2):
                    matching_func(cube,y,i)
                print(y[i]+y[i+1])
                paintCube(cube)
    
  

# --조건 및 입력 받는 부분----------------------------------------------------")
import time
input_list=['F','R','U','B','L','D',"'","2","Q"]
alphabet=['F','R','U','B','L','D']

keepgoing=True
paintCube(cube)
start=time.time()
count=0

while True:
    y = input('CUBE>').upper()
    
    for i in y:
        if i not in input_list:
            print('typing_error!')
            keepgoing=False
            break
        elif i=='Q':
            end=time.time()
            interval = time.localtime(end-start)
            print("경과시간:", time.strftime('%M:%S', interval))
            print("조작갯수:", count)
            print("이용해주셔서 감사합니다. 뚜뚜뚜.")
            keepgoing=False
            break
    if keepgoing==False:
        break
    perform_order(cube,y)



