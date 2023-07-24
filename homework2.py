# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число 
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть
print()
n = int(input("Введите количество монет: "))
averse_num = 0
for i in range(1, n+1):
    print("Если монета номер ", i, " лежит вверх решкой, то введите 1; иначе - введите 0:")
    current_coin = int(input())
    if (current_coin == 1): averse_num += 1
print("Положение всех монет определено: из ", n, " монет решкой вверх ", averse_num)
if (n - averse_num <= n/2): print("Минимум нужно перевернуть: ", n - averse_num)
else: print("Минимум нужно перевернуть: ", averse_num)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два 
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел 
# S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import math
print()
sum = int(input("Введите сумму 2-ух загаданных вами чисел: "))
mul = int(input("Введите произведение 2-ух загаданных вами чисел: "))
D = sum * sum - 4 * mul
x = (sum + math.sqrt(D))/2
y = sum - x
print("Загаданные вами числа равны: ", x, y)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
print()
n = int(input("Введите число N: "))
res = 1
for i in range(1, n+1):
    res = res * 2
    print("2 в степени " , i ," равняется ", res)