my_set1 = {'apple', 'lime', 'abc', 1 , 255}
my_set2 = {'apple', 'lime', 'abc', 1 , 255}

#two Set's have identical objects.
print(my_set1 == my_set2)

#Set's have different Id's becose it's 2 different objects in memory.
print(my_set1 is my_set2)
print(id(my_set1))
print(id(my_set2))

#chek object in set.
print('apple' in my_set1)