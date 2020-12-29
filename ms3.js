//*미션3
// Array 의 reduce 메서드처럼 동작하는 myReduce 메서드를 만들자.
// const myReduce = (arr, callback, initialValue) => {
//     //여기에 구현
// }
// const result = myReduce(arr, (next,prev) => {...}, []);
//-------------------------------------------------------------


let initialValue = 0;
const myReduce = (arr, callback, initialValue) => {
    callback()

}


const arr = [1, 2, 3, 4, 5];
const result = myReduce(arr, (next, prev) => {
    prev = 0;
    arr.forEach(function (el) {
        next = prev + el;
        prev = next;
    })
    return console.log(next);

}, []);