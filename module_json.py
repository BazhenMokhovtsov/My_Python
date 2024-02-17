import json

jason_str = '{"id": 524, "brand": "Nike", "qty": 210, "status": {"forSale": true}}'
jason_array = '[1, 2, 3, 4]'

my_dickt = {'id': 524,
 'brand': 'Nike',
 'qty': 210,
 'status': {
     'forSale': True
 }

}

sneakers = json.dumps(my_dickt, indent=4)

print('json',sneakers)

list_sneakers = json.loads(sneakers)
print('list_sneakers',list_sneakers)

my_list = json.loads(jason_array)
print( '\njason_array to python list', my_list)
