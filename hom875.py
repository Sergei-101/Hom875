import fractions
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input("Введите число - "))
examination_num = hex(num)
num_transformation = f"{num:#x}"
if examination_num == num_transformation:
    print(f"Задача решена верно, ответ - {num_transformation}")
else:
    print("Задача решена неправильно")

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


num_1 = int(input("Введите числитель первой дроби - "))
num_2 = int(input("Введите знаменатель первой дроби - "))
num_3 = int(input("Введите числитель второй дроби - "))
num_4 = int(input("Введите знаменатель второй дроби - "))
if num_3 != num_4:
    result_1 = f"{num_1 * num_4 + num_3 * num_2}/{num_2 * num_4}"
else:
    result_1 = f"{num_1 + num_3}/{num_4}"
result_2 = f"{num_1 * num_3}/{num_2 * num_4}"
result_3 = str((fractions.Fraction(num_1, num_2)) + fractions.Fraction(num_3, num_4))
result_4 = str((fractions.Fraction(num_1, num_2)) * fractions.Fraction(num_3, num_4))
if result_1 == result_3 and result_2 == result_4:
    print(f"Задача решена верно ответ {num_1}/{num_2} + {num_3}/{num_4} = {result_3}")
    print(f"Задача решена верно ответ {num_1}/{num_2} * {num_3}/{num_4} = {result_4}")
else:
    print("Задача решена неверно")