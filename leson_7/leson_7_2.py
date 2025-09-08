numbers = [23, 43, 75, 33, 80, 51, 62]
for number in numbers:
    print("Пучатаем: ", number)


for letter in "Кошка":
    print("Буква:", letter)


"""range(start, stop, step)"""


numbers = [23, 43, 75, 33, 80, 51, 62]
for i in range(len(numbers)):
    numbers[i] = 0
print(numbers)


words = ["Я " "люблю " "вкусно " "кушать)"]
result_str = ''

for word in words:
    result_str += ' ' + word
print(result_str)