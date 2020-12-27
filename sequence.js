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
const values = [];
const PI = Math.PI.toFixed(2);
let sum = 0;


function getArea(figure, r, r2, r3) {


    const area = {
        circle(r) {
            const result = PI * r ** 2;
            values.push(result);
        },
        rect(r, r2) {
            const result = r * r2;
            values.push(result);
        },
        trapezoid(r, r2, r3) {
            const result = (r + r2) * r3 / 2;
            values.push(result);
        }
    };
    area[figure](r, r2, r3);
    performed.push(figure);
}

function printExecutionSequence() {
    console.log('>계산수행순서 :', performed.join(', '));
    console.log('>함수결과값 :', values.join(', '));
}

getArea('circle', 2)
getArea('circle', 2)
getArea('circle', 2)
getArea('rect', 2, 3)
printExecutionSequence()