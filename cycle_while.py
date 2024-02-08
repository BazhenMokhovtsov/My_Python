import random


while True:
    answer = input("""Input yes or no
"""
                   )
    if answer == 'no':
        break


random_num = random.randint(1,5)
while True:
    num = int(input("Guess the num in range 1 - 5 "))
    if num != random_num:
        print("Try again.")
        continue
    print("Congratulations! ", random_num)
    break


#Chalenge
#Using cycle while we reques user input num 1 and num 2.
#check num 1 and num 2 for error
#If Error return Error text. Restarting cycle
#If no error exist return div num 1 and num 2
#ask user if they want to continue.
#if no break
#if yes continue
#используя цикл while мы просим ввести пользователя число 1 и число 2.
# эти числа проверяются на ошибку ввода.
#при ошибки, выводится Текст с описание ошибки. Цикл возабновляется.
#если ошибок нет выводим в терминал результат деления числа 1 на число 2
#спашиваем пользователя  хочет ли он продолжить.
#если нет, цикл прерывается.
#если да, цикл возабновляется.
def division_of_two_num():
    while True:
        try:
            num_one = float(input("Please enter first number: (to exit whrite [exit]) "))
            num_two = float(input("Please enter second number: (to exit whrite [exit]) "))
        except ValueError as e:
            print(e)
            print("Invalid input, please enter valid numbers. ")
            continue

        print(f"{num_one} / {num_two} = {num_one / num_two}")
        user_answer = input(" Continue ? ( yes/no ): ")
        if user_answer == 'yes':
            continue
        if user_answer == 'no':
            break


division_of_two_num()