const coffeeUL = document.getElementById("coffeeUL")
const emailTextBox = document.getElementById("emailTextBox")
const typeTextBox = document.getElementById("typeTextBox")
const sizeTextBox = document.getElementById("sizeTextBox")
const priceTextBox = document.getElementById("priceTextBox")
​
​
​
const saveButton = document.getElementById("saveButton")
​
​
​
​
saveButton.addEventListener('click', function() {
    const email = emailTextBox.value
    const type = typeTextBox.value
    const size = sizeTextBox.value
    const price = priceTextBox.value
​
    let request = new XMLHttpRequest()
    request.open('POST', 'https://troubled-peaceful-hell.glitch.me/orders')
    request.setRequestHeader('Content-Type', 'application/json')
    request.addEventListener('load', function() {
        console.log(this.resposeText)
        const coffee = JSON.parse(this.responseText)
        const coffeeItem = `<li class = "coffee">
        <b>${coffee.email}</b>
        <b>${coffee.type}</b>
        <b>${coffee.size}</b>
        <b>${coffee.price}</b>`
        coffeeUL.insertAdjacentHTML('beforeend', coffeeItem)
        console.log(coffee)
    })
    const body = {
        email: email,
        type: type,
        size: size,
        price: price
    }
    request.send(JSON.stringify(body))
})

deleteButton.addEventListener('click', function() {
    const deleteEmail = orderDelete.value

    let request = new XMLHttpRequest()
    request.open('DELETE', `https://troubled-peaceful-hell.glitch.me/orders/${DELETE}`) 
    request.onload = Function(){
        if [this.status == 200 $$ this.responseText== 4] 
        console.log(request.responseText)

        

    }
