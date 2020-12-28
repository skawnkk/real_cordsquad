//*미션1
//숫자타입으로만 구성된 요소를 뽑아 배열만들기
//실행결과
// ["width", "height", "hOffset", "vOffset", "size", "hOffset", "vOffset"]


const data = {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": {
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}


//for...in 2번 사용
const empty = [];
for (key in data) {
    const main_key = data[key];
    for (key2 in main_key) {
        const value = main_key[key2];
        if (typeof (value) === 'number') {
            empty.push(key2);
        }
    }
}
console.log(empty);


//foreach
const empty2 = [];
for (key in data) {
    const main_key2 = data[key];
    Object.keys(main_key2).forEach(function (el) {
        const value2 = main_key2[el]
        if (typeof (value2) === 'number') {
            empty2.push(el)
        }
    });
}
console.log(empty2);