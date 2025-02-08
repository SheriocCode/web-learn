console.log(1)
setTimeout(()=>{
    console.log(2)
    const p = new Promise((resolve, reject)=>{
        setTimeout(()=>{
            resolve(3)
        }, 2000)
    })
    p.then(result => {
        console.log(result)
    })
}, 0)

const p = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve(4)
    }, 2000)
})
p.then(result => {
    console.log(result)
})

const p2 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve(5)
    }, 2000)
})
