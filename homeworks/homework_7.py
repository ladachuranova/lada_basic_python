# """1"""
# from idlelib.squeezer import count_lines_with_wrapping
#
# N = int(input("Ввудите число:"))
# i = 1
# while i <= N:
#     i += 1
#
# print(i)
#
#
# """2"""
# N = int(input("Ввудите число:"))
# i = 1
# total = 0
# while i <= N:
#     if i % 2 == 0:
#         total += i
#     i += 1
# print("Сумма всех четных чисел от 1 до", N, "равна", total)
#
#
# """3"""
# num = int(input("Введите натураное число: "))
# count = 0
# while num > 0:
#     count += 1
#     num //= 10
# print("Количество цифр: ", count)
#
#
# """4"""
# num = int(input("Введите натураное число: "))
# max_n = 0
# while num > 0:
#         digit = num % 10
#         if digit > max_n:
#             max_n = digit
#         num //= 10
# print("Наибольшая цифра в числе:", max_n)
#
#
# """5"""
# password = ""
# while password != "qwerty123":
#     password = input("Введите пароль: ")
# print("Доступ разрешен")
#
#
#
# """1"""
# nums = [32, 88, 77, 75, 93, 22]
# i = 0
# while i < len(nums):
#     if nums[i] % 2 == 0:
#         print(num[i])
#         break
#     i += 1
# else:
#     print("Четное число не найдено")
#
#
# """2"""
# sum_n = 0
# nums = 1
# while nums > 0:
#     nums = int(input("Введите ччисло для прекращения нажмите 0: "))
#     if nums < 0:
#         continue
#     sum_n += nums
# print(sum_n)


"""3"""
a, b = map(int, input("Введите 2 числа через пробел: ").split())
while a <= b:
    a += 1
    if a % 2 != 0:
        print(a)
    else:
        continue


"""4"""
N = int(input("Введите число N: "))
if N <= 1:
    print(f"{N} не является простым числом")
else:
    divisor = 2
    while divisor * divisor <= N:
        if N % divisor == 0:
            print(f"{N} не является простым, делится на {divisor}")
            break
        divisor += 1
    else:
        print(f"{N} является простым числом")


"""5"""
max_number = None

while True:
    user_input = input("Введите число (0 для выхода): ")
    if user_input == "":
        break
    number = int(user_input)
    if number == 0:
        break
    if max_number is None or number > max_number:
        max_number = number
if max_number is not None:
    print(f"Наибольшее введенное число: {max_number}")
else:
    print("Числа не вводились")



"""1"""
word = input("Введите слово: ")
s = list(word)
s.reverse()
for s in s:
    print(s)


"""2"""
nums = [23, 65, 90, 76, 44]
for n in range(len(nums)):
    if n % 2 == 0:
        nums[n] = 0
print(nums)


"""2"""
N = int(input("Введите число N: "))
powers_of = []
for i in range(N+1):
    powers_of.append(2**i)
print(powers_of)


"""3"""
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
K = int(input("Введите шаг K: "))
for num in range(A, B + 1, K):
    print(num)
