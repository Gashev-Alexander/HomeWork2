num = int(input("Введите число N: "))
ar = {}
sum = 0
for n in range(1, num + 1):
    ar[n] = round(((1 + (1 / n)) ** n), 2)
    sum += ar[n]
print(ar)
print('Сумма элементов =', sum)