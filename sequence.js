//*미션2___printExecutionSequence 함수 만들기
//! 재귀함수 껴있는 경우는? ex)getArea(circle, 2,3)

// 프로그래밍에서 로깅(logging)은 프로그램의 수행과정이나 결과를 기록하는 것을 말한다.
// 지금까지 호출된 함수가 무엇인지 알려주는 printExecutionSequence함수를 만들자.

// getCircle() 
// getCircle() 
// getArea('circle',2) 
// getArea('rect',2,3) 
// printExecutionSequence()  //printExecutionSequence가 불려지면, 함수 호출된 순서를 출력한다. 
// > 계산수행순서 : circle, circle, circle, rect

const performed = [];

function getCircle() {
    performed.push('circle');
};

const PI = Math.PI;
let sum = 0;


function getArea(figure, r, r2, r3) {
    performed.push(figure);

    const area = {
        circle(r) {
            console.log(PI * r ** 2);
        },
        rect(r, r2) {
            console.log(r * r2);
        },
        trapezoid(r, r2, r3) {
            console.log((r + r2) * r3 / 2);
        }
    };
    area[figure](r, r2, r3);
}

function printExecutionSequence() {
    console.log('>계산수행순서 :', performed.join(', '));
}

getArea('circle', 2)
getArea('circle', 2)
getArea('circle', 2)
getArea('rect', 2, 3)
printExecutionSequence()