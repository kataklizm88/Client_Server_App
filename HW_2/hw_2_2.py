import json


def write_to_json(item, quantity, price, buyer, date):
    data = {
        item: 'item',
        quantity: 'quantity',
        price: 'price',
        buyer: 'buyer',
        date: 'date'
    }
    with open('orders.json') as f_n:
        json_load = json.load(f_n)
        x = json_load['orders']
        x.append(data)
    with open('orders.json', 'w') as f_n_w:
        json.dump(json_load, f_n_w, indent=4)

    return json_load

one = write_to_json('car', 12, 500, 'woman', '12.08.2000')
sec = write_to_json('house', 12, 500, 'woman', '12.08.2000')
print(one)
print(sec)






