async function getData() {
    try {
        const provinceData = await axios({url: 'http://localhost:3000/province'})
        const province = provinceData.data[0]
        const cityData = await axios({url: 'http://localhost:3000/city', params: province})
        const city = cityData.data[0]
    } catch (error) {
        console.log(error)
    }
}

getData()