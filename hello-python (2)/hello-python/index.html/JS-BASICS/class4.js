
//CALLBACKS

let counter = 0

window.setInterval(CALLBACK-Function, 5000)

const intervalId = window.setInterval(function() {
    counter++ 
    if(counter == 10) {
        // cancel the interval 
        window.clearInterval(intervalId)
        return 
    }
    console.log(counter)
}, 1000)


console.log(`Interval Id: ${intervalId}`)




const result = getStockQuote('GOOG')
console.log(result)

console.log()
