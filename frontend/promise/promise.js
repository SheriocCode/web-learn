// promise状态: pending -> resolved(fullfilled) -> rejected

const p = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve(1)
    }, 2000)
})

p.then(result => {
    console.log(result)
}).catch(err => {
    console.log(err)
})