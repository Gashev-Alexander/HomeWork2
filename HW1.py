def InputNumbers(inputText):
    usl = False
    while not usl:
        try:
            number = float(input(f"{inputText}"))
            usl = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите любое число: ")

print(f"Сумма цифр = {sumNums(num)}")