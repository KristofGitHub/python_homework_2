# Расчет факториала
# exit = 0
# while (exit == 0):
#     print()
#     n = int(input("Введите n: "))
#     res = 1
#     for i in range(1, n+1): res = res * i
#     print("Факториал n! = ", res)
#     exit_now = (input("Для выхода нажмите Q."))
#     if (exit_now == "q"): exit = 1
# print("Работа программы закончена.")
# print()

# Расчет функции Фибоначчи
print()
fib = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(2, 16):
    fib[i] = fib[i-1] + fib[i-2]
n = int(input("Введите n: "))
find = 0
for i in range(0, 16): print(i+1, " - ", fib[i])
for i in range(0, 16):
    if (n == fib[i]): 
        print("Введенное число является числом Фибоначчи, его номер в ряду равен ", i+1)
        find = 1
if (find == 0): print("Введенное число не является числом Фибоначчи.")
print("Работа программы закончена.")
print()