sum_1 = 1 + 2 + 3 + 4 + 5
print(sum_1)


num = 1000
sum_2 = 0
i = 1
while i <= 1000:
    sum_2 += i
    i += 1
print(sum_2)


correct_password = "Пароль123"
input_password = input("Введите пароль:")
counter = 1

while input_password != correct_password:
    print(f"Пароль не праильный, осталось попыток {counter}")
    input_password = input("Введите пароль:")
    counter += 1
    if counter == 3:
        print("Пароль введен максимально раз")
        break

print("Пароль верный")


numbers = [23, 43, 33, 80, 51, 62]
result = []
i = 0
while True:
    if numbers[i] % 2 == 0:
        result.append(numbers[i])
    i += 1
    if i == len(numbers):
        break
print(result)


num = 1
res_sum = 0
while num != 0:
    num = input("Введите число или 0 для выхода: ")
    if not input_password.isdigit():
        print("Только числа")
        break
    num = int(input_password)
    if num % 2 == 0:
        continue
    res_sum += num
else:
    print(res_sum)