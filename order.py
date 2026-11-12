def order_sum(order):
    total = 0
    for i in order:
        if i["price"] < 1000:
            continue
        total += i["quantity"] * i["price"]
    return total
order = [
        {"customer":"asha","quantity":2,"price":1200},
        {"customer":"rahul","quantity":6,"price":1700},
        {"customer":"golu","quantity":1,"price":100},
        {"customer":"raj","quantity":7,"price":2700}
    ]
print(order_sum(order))