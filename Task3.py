# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

N = int(input('Введите число:'))

for i in range(1,N+1,1):
    x = (1+1/i)**i
    print(x)