//*미션1__getArea

const PI = Math.PI;
let sum = 0;


function getArea(figure, r, r2, r3) {

    const area = {
        circle(r, r2) {
            if (!r2) {
                console.log(PI * r ** 2);
            } else {
                if (r > r2) {
                    return console.log(sum);
                } else {
                    const result = PI * r ** 2;
                    sum += result;
                }
                getArea('circle', r + 1, r2);
            }
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

getArea('circle', 10);
getArea('rect', 10, 15);
getArea('trapezoid', 10, 15, 12);
getArea('circle', 1, 3);
// 반지름이 1 부터 n까지 1 씩 증가하면서
// n개까지의 원의 넓이의 모든 합을 출력.(재귀적인 해결책을 제시한다)