my_fruits = ['apple', 'banana', 'lime']

#Syntax for ... in ... => for "element" in "sequences":
my_list = [True, 154, 'world']

#for element in my_list:
#    print(element)

my_video = {'1920x180', True, 54, False, 'hi', 124}

#for elem in my_video:
#    print(elem)

my_object = {
    'first': 10,
    'second': "Value",
    'third': False
}

#for key in my_object:
#    print(key, my_object[key])

#Method items() return tuple sequence
#We can unpacking tuple sequens for 2 variables, key and value.
#for item in my_object.items():
#    keys, value = item #unpacking tuple.
#    print(keys,value)

#set is not a fixed sequence
#for info in my_video:
#    print(info)

#for num in range(5):
#    print(num)

#Example 1
def dict_to_list(dict_to_convert):
    list_for_conversion = []
    for item in dict_to_convert.items():
        key1 , value1 = item
        value1 = value1 * 2 if type(value1) == int and value1 % 2 == 0 else value1
        list_for_conversion.append((key1, value1))
    return list_for_conversion

my_dict = {
    'id': 1,
    'User': "2",
    'Tel.': 3.5,
    'Old': 4,
    'year':5,
    'num': 6.1
}
#print(dict_to_list(my_dict))


def filter_my_list(list_to_filter, value_type):
    print(list_to_filter)
    result_list = []
    for element in list_to_filter:
        if type(element) == value_type:
            result_list.append(element)
    return result_list

print(filter_my_list(my_list,str))
