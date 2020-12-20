//todo: 함수오류 수정 (F부분 부터)
//todo: 게임종료 구현 (시간, COUNT(최종 배열의 길이))
//TODO: 게임완성 시 축하메시지
//TODO: 큐브 믹스 기능 추가

console.log("linked")

const printArea = document.querySelector(".printCube");
const topFace = printArea.querySelector(".top");
const leftSide = printArea.querySelector(".left");
const frontSide = printArea.querySelector(".front");
const rightSide = printArea.querySelector(".right");
const backSide = printArea.querySelector(".back");
const bottom = printArea.querySelector(".bottom");
const orderedList = [];
const nextOrder = [];

const arr =[[],[],[],[],[],[]];
const empty=[[],[],[],[],[],[]];
const colors=['B','W','O','G','Y','R'];

for (i=0; i<6; i++){
    let j = 0;
    while (j<3){
        empty[i].push(colors[i]);
        j++;
    }

    let k =0;
    while (k<3){
        arr[i].unshift(empty[i]);
        k++;
    }
}

function quit(){
    console.log('그만하세..');
}
function ctrlZ(){
    const currIndex = orderedList.length-1;
    const status = orderedList[currIndex];
    nextOrder.unshift(orderedList.pop());
    console.log(orderedList, nextOrder);
    performOrder(status[0], status[1] ? repeat=1 : repeat=3);
    orderedList.pop()
    
    console.log(orderedList, nextOrder);
}

function ctrlY(){
    console.log(orderedList, nextOrder);
    const status = nextOrder.shift();
    performOrder(status[0], status[1] ? repeat=3 : repeat=1);
}

function linkedFace(arr, n){
    target = arr[n][0][0];
    arr[n][0][0] = arr[n][2][0];
    arr[n][1][0] = arr[n][2][1];
    arr[n][2][0] = arr[n][2][2];
    arr[n][2][1] = arr[n][1][2];
    arr[n][2][2] = arr[n][0][2];
    arr[n][1][2] = arr[n][0][1];
    arr[n][1][2] = target;
};

//todo:함수오류 수정
function performOrder(order, repeat){
    console.log(order);

    const orderList = {
        U(){
            target = arr[2][0];
            arr[2][0] = arr[3][0];
            arr[3][0] = arr[4][0];
            arr[4][0] = arr[1][0];
            arr[1][0] = target;
            linkedFace(arr, 0);
        },
        D(){
            target = arr[2][2];
            arr[2][2] = arr[1][2];
            arr[1][2] = arr[4][2];
            arr[4][2] = arr[3][2];
            arr[3][2] = target;
            linkedFace(arr, 5);
        },
        R(){
            target = arr[2][0][2], arr[2][1][2], arr[2][2][2];
            arr[2][0][2], arr[2][1][2], arr[2][2][2] = arr[5][0][2], arr[5][1][2], arr[5][2][2];
            arr[5][0][2], arr[5][1][2], arr[5][2][2] = arr[4][2][0], arr[4][1][0], arr[4][0][0];
            arr[4][2][0], arr[4][1][0], arr[4][0][0] = arr[0][0][2], arr[0][1][2], arr[0][2][2];
            arr[0][0][2], arr[0][1][2], arr[0][2][2] = target;
            linkedFace(arr, 3);
        },
        L(){
            target = arr[2][0][0], arr[2][1][0], arr[2][2][0];
            arr[2][0][0], arr[2][1][0], arr[2][2][0] = arr[0][0][0], arr[0][1][0], arr[0][2][0];
            arr[0][0][0], arr[0][1][0], arr[0][2][0] = arr[4][2][0], arr[4][1][0], arr[4][0][0];
            arr[4][2][0], arr[4][1][0], arr[4][0][0] = arr[5][0][0], arr[5][1][0], arr[5][2][0];
            arr[5][0][0], arr[5][1][0], arr[5][2][0] = target;
            linkedFace(arr, 1);
        },
        F(){
            target = arr[0][2][0], arr[0][2][1], arr[0][2][2];
            arr[0][2][0], arr[0][2][1], arr[0][2][2] = arr[1][2][2], arr[1][1][2], arr[1][0][2];
            arr[1][2][2], arr[1][1][2], arr[1][0][2] = arr[5][0][2], arr[5][0][1], arr[5][0][0];
            arr[5][0][2], arr[5][0][1], arr[5][0][0] = arr[3][0][0], arr[3][1][0], arr[3][2][0];
            arr[3][0][0], arr[3][1][0], arr[3][2][0] = target;
            linkedFace(arr, 2);
        },
        B(){
            target = arr[0][0][0], arr[0][0][1], arr[0][0][2];
            arr[0][0][0], arr[0][0][1], arr[0][0][2] = arr[3][0][2], arr[3][1][2], arr[3][2][2];
            arr[3][0][2], arr[3][1][2], arr[3][2][2] = arr[5][2][2], arr[5][2][1], arr[5][2][0];
            arr[5][2][2], arr[5][2][1], arr[5][2][0] = arr[1][2][0], arr[1][1][0], arr[1][0][0];
            arr[1][2][0], arr[1][1][0], arr[1][0][0] = target;
            linkedFace(arr, 4);
        }
    }
    for(let i=0; i<repeat; i++){
        orderList[order]();
    }
    expression(arr);
    repeat===3 ? orderedList.push(order+"'") : orderedList.push(order);
    console.log(orderedList);
}
////명령 버튼 클릭 및 처리
function readOrder(event){
    const order = event.path[0].innerText;
    const basicOrder = ["U","D","F","B","R","L"];

    if (!order[1]){       
        order==="◀" && ctrlZ();
        order==="▶" && ctrlY();
        basicOrder.includes(order) && performOrder(order,1);
    } else {
        order[1]==="'" && performOrder(order[0],3);
        order==="종료" && quit();
    }
}

//// 초기큐브 구현
function expression(arr){
    topFace.innerText= arr[0][0].join(" ")+"\n"+arr[0][1].join(" ")+"\n"+arr[0][2].join(" ");
    leftSide.innerText= arr[1][0].join(" ")+"\n"+arr[1][1].join(" ")+"\n"+arr[1][2].join(" ");
    frontSide.innerText= arr[2][0].join(" ")+"\n"+arr[2][1].join(" ")+"\n"+arr[2][2].join(" ");
    rightSide.innerText= arr[3][0].join(" ")+"\n"+arr[3][1].join(" ")+"\n"+arr[3][2].join(" ");
    backSide.innerText= arr[4][0].join(" ")+"\n"+arr[4][1].join(" ")+"\n"+arr[4][2].join(" ");
    bottom.innerText= arr[5][0].join(" ")+"\n"+arr[5][1].join(" ")+"\n"+arr[5][2].join(" ");   
}

function init(){
    expression(arr);
    const orderBtn = document.querySelectorAll("button");
    for(let i=0; i<orderBtn.length;i++){
        orderBtn[i].addEventListener("click",readOrder);
    }
}

init();


