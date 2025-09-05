"""1"""
x = int(input("Число: "))
if x > 0:
    print("Число положительное")
elif x < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")


"""2"""
x = int(input("Число: "))
if x % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")


"""3"""
x = int(input("Число: "))
if 1 < x < 10:
    print("Число в диапазоне")
else:
    print("Число вне диапазона")


"""4"""
a = int(input("Число: "))
b = int(input("Число: "))
if a < b:
    a, b = b, a
print(a, b)


"""5"""
a = int(input("Число: "))
b = int(input("Число: "))
if a < b:
    print(a)
else:
    print(b)


"""6"""
marks = [3, 4, 5, 2, 5, 4]
if 2 in marks:
    print("Есть неудовлетворительная оценка")
else:
    print("Все оценки положительные")


"""7"""
num = int(input("Число: "))
x = int(input("Введите число: "))

if x % 3 == 0 and x % 5 == 0:
    print("Число делится на 3 и 5")
elif x % 3 == 0:
    print("Число делится только на 3")
elif x % 5 == 0:
    print("Число делится только на 5")
else:
    print("Число не делится на 3 и 5")


"""8"""

password = input("Введите пароль: ")
if password == "admin123":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")


"""9"""
amount = float(input("Число: "))
if amount >= 5000:
    discount = 0.10
    print("скидка 10%")
elif amount >= 1000:
    discount = 0.05
    print("скидка 5%")
else:
    discount = 0.0
final_amount = amount * (1 - discount)
print("Итоговая сумма после скидки:", final_amount)


"""10"""
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Год високосный")
else:
    print("Год не високосный")



"""1"""
grade = int(input("Введите оценку (от 1 до 5): "))
if grade == 5:
    print("Отлично!")
elif grade == 4:
    print("Хорошо")
elif grade == 3:
    print("Удовлетворительно")
elif grade == 2 or grade == 1:
    print("Неудовлетворительно")
else:
    print("Некорректная оценка")


"""2"""
hour = int(input("Введите текущее время (0-23): "))

if 6 <= hour <= 11:
    print("Утро")
elif 12 <= hour <= 17:
    print("День")
elif 18 <= hour <= 21:
    print("Вечер")
elif (22 <= hour <= 23) or (0 <= hour <= 5):
    print("Ночь")
else:
    print("Некорректное время")


"""3"""
temperature = float(input("Введите температуру: "))

if temperature < -10:
    print("Очень холодно")
elif -10 <= temperature <= 0:
    print("Холодно")
elif 1 <= temperature <= 10:
    print("Прохладно")
elif 11 <= temperature <= 25:
    print("Тепло")
elif temperature > 25:
    print("Жарко")


"""4"""
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")


"""5"""
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == '+':
    print("Результат:", num1 + num2)
elif operation == '-':
    print("Результат:", num1 - num2)
elif operation == '*':
    print("Результат:", num1 * num2)
elif operation == '/':
    if num2 != 0:
        print("Результат:", num1 / num2)
    else:
        print("Ошибка: деление на ноль!")
else:
    print("Некорректная операция")


"""1"""
num = int(input("Введите число: "))
result = "Чётное" if num % 2 == 0 else "Нечётное"
print(result)


"""2"""
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
max_num = a if a > b else b
print("Наибольшее число:", max_num)


"""3"""
num = int(input("Введите число: "))
result = "Положительное" if num > 0 else ("Отрицательное" if num < 0 else "Ноль")
print(result)


"""4"""
age = int(input("Введите ваш возраст: "))
message = "Вход разрешен" if age >= 18 else "Вход запрещен"
print(message)


"""5"""
amount = float(input("Введите сумму покупки: "))
final_amount = amount * 0.9 if amount > 5000 else amount
print("Итоговая сумма после скидки:", final_amount)