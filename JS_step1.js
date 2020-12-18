////1: 파라미터 단어 재 선택: move -> movedWord 수정
////2: 함수 간결하게 써보기 (->thenary_operator)
//todo3: false msg보내기

const inputForm = document.querySelector('.submit');
const input = inputForm.querySelector('input');
const submitBtn = inputForm.querySelector('button');
const printArea = inputForm.querySelector('span');

function print(movedWord){
    console.log(movedWord.join(''))
    printArea.innerText= movedWord.join('');
    printArea.classList.remove('on');
}

function moveRight(word, count){
    const movedWord = word.split('');
    for (let i=0; i<Math.abs(count); i++){
        movedWord.unshift(movedWord.pop());
    }
    print(movedWord);
}

function moveLeft(word, count){
    const movedWord = word.split('');
    console.log(movedWord, count)

    for (let i=0; i<Math.abs(count); i++){
        movedWord.push(movedWord.shift());
        console.log(movedWord, count)
    }
    
    print(movedWord);
}

function move(inputArr){
    const word = inputArr[0];
    const count = Number(inputArr[1]);
    const direction = inputArr[2].toUpperCase();
    
    if (count>0){
        direction === 'R'
        ? moveRight(word, count)
        : moveLeft(word, count);
    } else {
        direction === 'R'
        ? moveLeft(word, count)
        : moveRight(word, count);
    }
}

const inputCheck2 = {
    count : function(count){
        if ((count-Math.floor(count))===0){
            return true;
        } else {
            return false;
        };
    },
    direction : function(direction){
        if (direction){
            direction = direction.toUpperCase();
            if (direction==='R'|| direction==='L'){
                return true;
            } else {
                return false;
            }
        } else{
            return false;
        }
    }
}

function inputCheck(inputValue){
    const inputArr = inputValue.split(' ');
    const checkCount = inputCheck2.count(Number(inputArr[1]));
    const checkDirection = inputCheck2.direction(inputArr[2]);

    if (checkCount === true && checkDirection === true){
        move(inputArr);
    } else{
        printArea.innerText='입력조건이 맞는지 다시 확인해주세요.'
    }
}

function handleSubmit(event){
    event.preventDefault();
    const inputValue = input.value;    
    inputCheck(inputValue);
}


input.addEventListener("submit", handleSubmit);
submitBtn.addEventListener("click",handleSubmit);
