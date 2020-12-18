//todo: printCube하고나서 입력창에 값 지워주기.
//todo: 예쁜 화살표있으면 프린트큐브에 붙여넣어주기
//TODO: 게임종료시 alert msg -> 확인 취소
//todo: 확인-> 작동한 printCube 삭제하기, 
//todo: 타이핑에러처리.

const inputForm = document.querySelector(".submit");
const submitInput = inputForm.querySelector("input");
const submitBtn = inputForm.querySelector("button");
const printArea = document.querySelector(".printArea");
const cube = [['R', 'R', 'W'], ['G', 'C', 'W'], ['G', 'B', 'B']];

function moveCube(order,repeat){
    const tasks = {
        U(){
            for (let i = 0; i<repeat; i++){
                cube[0].push(cube[0].shift());
            };
            expression(cube, order, repeat);
        },
        B(){
            for (let i = 0; i<repeat; i++){
                cube[2].unshift(cube[2].pop());
            };
            expression(cube, order, repeat);
        },
        R(){
            const arr=[];
            for (let i = 0; i<repeat; i++){
                for (let j = 0; j<3; j++){
                    arr.push(cube[j].pop());
                }
                arr.push(arr.shift());
                for (let k = 0; k<3; k++){
                    cube[k].push(arr.shift());
                }
            };
            expression(cube, order, repeat);
        }, 
        L(){
            const arr=[];
            for (let i = 0; i<repeat; i++){
                for (let j = 0; j<3; j++){
                    arr.push(cube[j].shift());
                }
                arr.unshift(arr.pop());
                for (let k = 0; k<3; k++){
                    cube[k].unshift(arr.shift());
                }
            };
            expression(cube, order, repeat);
        },    
        Q(){
            alert('큐브 작동을 종료합니다?\n작동한 큐브가 사라집니다.');
            
        }
    };

    tasks[order]();
    
}

function inputChecking(inputedOrder){
    const orderList=["R","R'","L","L'","U","U'","B","B'","Q"];
    const special="'";
    const inputArr = inputedOrder.split(' ');
    inputArr.forEach(order=>{
        if (orderList.includes(order)){
            if (order[1]){
                moveCube(order[0], 2);
            }else{
                moveCube(order, 1);
            }
        } else{
            console.log('typing_error');
        }
    });   
}

function handleSubmit(event){
    event.preventDefault();
    const inputedOrder = submitInput.value.toUpperCase();
    inputChecking(inputedOrder);
}

function expression(cube, order, repeat){
    const printOrder = document.createElement("div");
    const printCube = document.createElement("div");
    const div=document.createElement("div");
    div.classList.add("parentDiv");
    div.append(printOrder);
    div.append(printCube);
    printArea.append(div);
    
    if (order && repeat===2){
        printOrder.innerText = order+"'";
    } else if (order && repeat===1){
        printOrder.innerText = order;
    } else {
        printOrder.innerText = 'Start';
    };
    
    printCube.innerText = `${cube[0].join('')}\n${cube[1].join('')}\n${cube[2].join('')}`;
}

inputForm.addEventListener("submit",handleSubmit);
submitBtn.addEventListener("click",handleSubmit);
expression(cube);