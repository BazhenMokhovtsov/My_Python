# Chalenge
my_dict = {
    'a': 'first',
    'b': 'second',
    'c': 'third',
    'smal': 'hi'
}

my_list = ['hi', 'Hallo', 'Banana']
scores = {k: v.upper() for k, v in my_dict.items()}


long_strings = [elem for elem in my_list if len(elem) > 3]
print(long_strings, scores)
# Chelenge end.


all_nums = [-1, -2, 3, -4, 5]

absolut_num = []
for num in all_nums:
    absolut_num.append(abs(num))


absolut_nums = [abs(num) for num in all_nums]

positiv_num = []
for num in all_nums:
    if num > 0:
        positiv_num.append(num)

positiv_nums = [num for num in all_nums if num > 0]

my_set = {1 ,5 , 11}

new_set = {val * val for val in my_set}

my_scores = {
    'a': 10,
    'b': 23,
    'c': 44,
}

scores = {k: v * 10 for k, v in my_scores.items()}

scoress = {k: v for k, v in enumerate(my_set)}

