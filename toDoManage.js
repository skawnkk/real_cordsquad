//  미션. 할일관리 프로그램
//  **todos.js ** 함수에 대한 설계와 코드구현을 한 후 이를 PR한다.
//  todos.js 에서는 show 함수가 두 번 불린다.
//  따라서 다음과 같이 두 개의 결과가 나와야 한다.
//  $ nodejs todos.js
//  현재상태 :  todo: 1개, doing:2개, done:4개
//  todo리스트 :  총3건 : ' 자바스크립트 공부하기' , 'iOS공부하기'

//todos.js

const todos = [{
        'name': '자바스크립트 공부하기',
        'tags': ['programming', 'javascript'],
        'status': 'todo',
        'id': 12123123
    },
    {
        'name': ' 그림 그리기',
        'tags': ['picture', 'favorite'],
        'status': 'doing',
        'id': 312323
    },
    {
        'name': ' iOS공부하기',
        'tags': ['programing', 'favorite'],
        'status': 'todo',
        'id': 301220
    },
    {
        'name': ' 영어 공부하기',
        'tags': ['english', 'favorite'],
        'status': 'done',
        'id': 3012201
    }
];

const dataObj = {
    "todo": [],
    "doing": [],
    "done": []
}

const dataInput = (todos) => {
    todos.forEach(value => {
        if (value.status === 'todo') dataObj.todo.push(value.name);
        if (value.status === 'doing') dataObj.doing.push(value.name);
        if (value.status === 'done') dataObj.done.push(value.name);
    });
}

const show = (obj) => {
    if (obj === "all") {
        console.log("현재상태__ todo:", dataObj.todo.length, "개", " doing:", dataObj.todo.length, "개", " done:", dataObj.todo.length, "개");
    }
    if (dataObj[obj] !== undefined) {
        console.log(obj, '리스트: 총 갯수:', dataObj[obj].length, "건,", dataObj[obj].join(","));
    } else {
        console.log("입력값이 잘못되었습니다.")
    }
}

dataInput(todos);
show("all");
show("todo");
show("doing");
show("hi");