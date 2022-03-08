from functools import reduce

def reducer(acc, val):
    acc.extend(val['orderedProduct'])
    return acc

def red_2(acc, val):
    if val['productId'] in acc:
        acc[val['productId']]+=val['quantity']
    else:
        acc[val['productId']]=val['quantity']
    return acc
data = [
        {
            "orderedProduct": [
                {
                    "productId": "6217b119c78e5324bf1d6358",
                    "quantity": 3,
                },
                {
                    "productId": "6217b119c78e5324bf1d6359",
                    "quantity": 1,
                }
            ]
        },
        {
            "orderedProduct": [
                {
                    "productId": "6217b119c78e5324bf1d6358",
                    "quantity": 2,
                },
                {
                    "productId": "6217b119c78e5324bf1d6359",
                    "quantity": 3,
                }
            ]
        }
    ]

reduced_arr = reduce(reducer, data, [])
final = reduce(red_2, reduced_arr, {})
print(final)