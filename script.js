const response = {
    "status": "done",
    "message": [
        {
            "orderedProduct": [
                {
                    "_id": "6225fc50d6b29b5603af4a2d",
                    "productId": "6217b119c78e5324bf1d6358",
                    "quantity": 3,
                    "subtotal": 8250
                },
                {
                    "_id": "6225fc50d6b29b5603af4a2e",
                    "productId": "6217b119c78e5324bf1d6359",
                    "quantity": 1,
                    "subtotal": 3500
                }
            ]
        },
        {
            "orderedProduct": [
                {
                    "_id": "6225fc50d6b29b5603af4a2f",
                    "productId": "6217b119c78e5324bf1d6358",
                    "quantity": 2,
                    "subtotal": 5500
                },
                {
                    "_id": "6225fc50d6b29b5603af4a30",
                    "productId": "6217b119c78e5324bf1d6359",
                    "quantity": 3,
                    "subtotal": 10500
                }
            ]
        }
    ]
}
const fetchProductQuantities = (orders) => {
    const result = {};
    for ( order of orders ){
        for ( product of order['orderedProduct'] ) {
            if (result[product['productId']]) {
                result[product['productId']] += product['quantity']
            } else {
                result[product['productId']] = product['quantity']
            }
        }
    }
    return result
}
//console.log(fetchProductQuantities(response.message))

const bankAccounts = []

function createAccount(username, balance) {
    account = {
        username: username,
        balance: balance
    }
    bankAccounts.push(account)
}

function getAccount(username) {
    //Loops through the bankAccounts array and check for an account that matches the specified username
    for (account of bankAccounts) {
        if (account.username == username){
            return account
        }
    }
    console.log("Account Not Found")
    return null
}

function withdraw(username, amount){
    for (i=0; i<bankAccounts.length; i++){
        account = bankAccounts[i]
        if (account.username == username){
            if (account.balance >= amount) {
                account.balance -= amount
                bankAccounts[i] = account
                return account
            }
            console.log("Insufficient Balance")
            return account
        }
    }
    console.log("Account Not Found")
    return null
}

function deposit(username, amount){
    for (i=0; i<bankAccounts.length; i++){
        account = bankAccounts[i]
        if (account.username == username){
            account.balance += amount
            bankAccounts[i] = account
            return account
        }
    }
    console.log("Account Not Found")
    return null
}

function getBalance(username) {
    for (account of bankAccounts) {
        if (account.username == username){
            return account.balance
        }
    }
    console.log("Account Not Found")
    return null
}

function getBankBalance() {
    total = 0
    for (account of bankAccounts) {
        total += account.balance
    }
    return total
}

createAccount("Teepy", 2000)
createAccount("Kelpy", 5000)
console.log(withdraw("Teepy", 3000))
console.log(withdraw("Teepy", 2000))
console.log(deposit("Teepy", 2000))
console.log(getAccount("Teepy"))
console.log(getBalance("Teepy"))
console.log(getBankBalance())