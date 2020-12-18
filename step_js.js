////1: 파라미터 단어 재 선택: move -> movedWord 수정
////2: 함수 간결하게 써보기 (->thenary_operator)
//todo3: false msg보내기

const inputForm = document.querySelector('.submit');
const input = inputForm.querySelector('input');
const submitBtn = inputForm.querySelector('button');
const printArea = inputForm.querySelector('span');

function print(movedWord){
    printArea.innerText= movedWord.join('');
}

function moveRight(word, count){
    const movedWord = word.split('');
    for (let i=0; i<count; i++){
        movedWord.unshift(movedWord.pop());
    }
    print(movedWord);
}

function moveLeft(word, count){
    const movedWord = word.split('');
    for (let i=0; i<-count; i++){
        movedWord.push(movedWord.shift());
    }
    print(movedWord);
}

function inputCheck(inputValue){
    const inputArr = inputValue.split(' ');
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

function handleSubmit(event){
    event.preventDefault();
    const inputValue = input.value;    
    inputCheck(inputValue);
}


input.addEventListener("submit", handleSubmit);
submitBtn.addEventListener("click",handleSubmit);

