const xhr = new XMLHttpRequest();
xhr.open('POST', 'http://127.0.0.1:5000/stream_chat')
xhr.addEventListener('loadend',()=>{
    console.log(xhr.responseText)
})

// 设置请求头
xhr.setRequestHeader("Content-Type", "application/json");

const obj = {
    "username": "user1",
    "password": "123456"
}

// 发送请求
xhr.send(JSON.stringify(obj))