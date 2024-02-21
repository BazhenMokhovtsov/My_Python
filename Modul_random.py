import random

print(random.random())
print(random.randint(1, 10))


print(random.choice('abcdefg'))
print(random.choice([1, 2, 3]))

print(random.choices([1, 2, 3, 4, 5, 6], k=2))
my_list = [1, 2, 3, 4, 5, 6]
print(random.shuffle(my_list))
print(my_list)

print(''.join(random.choices('123456', k=5)))
