
# -루빅큐브 초기상태 평면도 구현---------------------------------------------

cube = [[] for _ in range(6)]
for _ in range(3):
    cube[0].append(['B','B','B'])    
    cube[1].append(['W','W','W'])
    cube[2].append(['O','O','O'])
    cube[3].append(['G','G','G'])
    cube[4].append(['Y','Y','Y'])
    cube[5].append(['R','R','R'])

for i in range(3):  
    for j in range(3):
        print(cube[0][i][j], end="")
    print()
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


# -입력함수처리 및 함수매칭----------------------------------------------------

def matching_func(y, i, repeat):
    print('hello')

def perform_order(y):

    for i in range(len(y)):
        if (len(y)==1 and i==0) or (i==len(y)-1):
            matching_func(y,i,repeat)

        elif len(y)>1 and i<len(y)-1:
            if y[i] in alphabet and y[i+1] in alphabet:
                matching_func(y,i,repeat)
                    
            elif y[i] in alphabet and y[i+1]=="'":
                repeat=3
                matching_func(y,i,repeat)

            elif y[i] in alphabet and y[i+1]=="2":
                repeat=2

# --조건 및 입력 받는 부분----------------------------------------------------")
order=['F','R','U','B','L','D',"'","2"]
alphabet=['F','R','U','B','L','D']
repeat=1
keepgoing=True

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
    perform_order(y)
