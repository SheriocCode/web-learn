const name = 'zhangsan'
const sum = function(a, b){
    console.log(a+b)
}

// 默认导出
// export default {
//     name,
//     sum
// }

// 命名导出
export const func = function(){
    console.log('func')
}