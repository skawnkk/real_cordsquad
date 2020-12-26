//*미션
//*여러개의 인자를 입력할 땐 공백으로 구분해낸다.
//*숫자가 아니면 에러를 반환하도록 구현한다.
//*인자의갯수가 부족하면 에러를 반환한다.

//*반지름을 입력받아 원의 넓이를 계산하는 함수를 만든다.
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const PI = Math.PI;

let input = [];


// rl.question('radius of a circle:', (r) => {
//     if (Number(r) || false) {
//         const areaCircle = PI * r ** 2
//         console.log(areaCircle);
//     } else {
//         console.log('🟥error__정수를 입력해주세요.');
//     }
//     rl.close();
// });

//*필요한 인자를 입력받아 사각형의 넓이를 계산하는 함수를 만든다.
// rl.question('length of square side:', (r) => {
//     if (Number(r) || false) {
//         const areaSquare = r ** 2
//         console.log(areaSquare);
//     } else {
//         console.log('🟥error__정수를 입력해주세요.');
//     }
//     rl.close();
// })


//*필요한 인자를 입력받아 사다리꼴의 넓이를 계산하는 함수를 만든다.

// rl.question('upper bottom_length height:', function (line) {
//     input = line.split(' ').map((el) => Number(el));
//     if ((input[0] && input[1] && input[2]) || false) {
//         const areaTrapezoid = (input[0] + input[1]) * input[2] / 2
//         console.log(areaTrapezoid);
//     } else {
//         console.log('❗error__3개의 인자, 정수입력하기')
//     }
//     rl.close();
// })

//*필요한 인자를 입력받아 원기둥의 넒이를 계산하는 함수를 만든다.

rl.question('radius height:', function (line) {
    input = line.split(' ').map((el) => parseInt(el))
    if ((input[0] && input[1]) || false) {
        const areaCylinder = 2 * PI * input[0] * input[1] + PI * input[0] ** 2;
        console.log(areaCylinder);
    } else {
        console.log('❗error__2개의 인자, 정수입력하기')
    }
    rl.close();
})