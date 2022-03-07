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

console.log(fetchProductQuantities(response.message))