nums = [11, 2, 15, 7]
target = 9



for i in range(len(nums)): # перебор индексов списка
    for j in range(i + 1, len(nums)): # перебор оставшихся индексов в списке
        if nums[i] + nums[j] == target: # сравнение суммы 2х эелементов в списке на равенсто Таргету
            print(i, j)




nums = [5, 7, 2, 1, 4, 6, 8, 3]
count_iter = 0
for i in range(len(nums)): # перебор индексов
    min_value = i # обьявляем переменную и записываем первый элемент списка как минимальный
    for j in range(i + 1, len(nums)): # перебор по оставшимся индексам
        if nums[j] < nums[min_value]: # сравниваем сущ. мин. значение с оставшимися в списке.
            min_value = j # переписываем минимальное значение
            # print(nums)
            print(nums[i], 'change to', nums[min_value], '|', nums)
            print('circle cycle number:', count_iter)

    nums[i], nums[min_value] = nums[min_value], nums[i] #изменяем позицию текущего мин. Значение на новое мин.значение.
    count_iter += 1
print(nums)
