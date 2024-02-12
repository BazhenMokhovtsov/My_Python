from sys import getsizeof

squares_gen = (num * num for num in range(10000))
print(getsizeof(squares_gen))
#208

squares_list = [num * num for num in range(10000)]
print(getsizeof(squares_list))

squares_gen = (num * num for num in range(10000)) # Create generator

# Iteration counting and whrite iteretion and value in dict.
my_dict = {}
count = 0
for elem in squares_gen:
    count += 1

    if elem not in my_dict:
        my_dict[elem] = count - 1

    if elem >= 101:
        break
    print(my_dict)