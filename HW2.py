def InputNumbers(inputText):
    usl = False
    while not usl:
        try:
            number = int(input(f"{inputText}"))
            usl = True
        except ValueError:
            print("Это так не работает!")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


n = InputNumbers("Введите число для расчета набора произведений: ")

list = []
for e in range(1, n + 1):
    list.append(mult(e))

print(f"Набор произведений чисел от 1 до {n}:  {list}")