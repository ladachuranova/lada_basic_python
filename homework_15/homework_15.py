"""1"""
# with open("data.txt", "r", encoding="utf-8") as f:
#      print(f.read())


# """2"""
# with open("data.txt", "r", encoding="utf-8") as f:
#     print(f.readline())
#
#
# """3"""
# with open("data.txt", "r", encoding="utf-8") as f:
#      print(f.read(10))
#
#
# """4"""
# with open("data.txt", "r", encoding="utf-8") as f:
#     print(f.readlines())
#
#
# """5"""
# with open("data.txt", "r", encoding="utf-8") as f:
#         print( "Строка: ", f.readline(), end='')
#         print("Строка: ", f.readline(), end='')
#         print("Строка: ", f.readline(), end='')


"""6"""
with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read(5))
    f.seek(0)
    print(f.read(5))


"""7"""
import os
f = os.path.getsize('data.txt')
print(f)


"""8"""
with open("data.txt", "r", encoding="utf-8") as f:
     print(f.read())


"""9"""
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        text = f.read()
        print(text)

except FileNotFoundError:
        print("Файл не найден")


"""11"""
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
except FileNotFoundError:
    print("Ошибка: Файл не найден")


"""12"""
try:
    with open("numbers.txt.py", encoding="utf-8") as f:
        total = 0
        for line in f:
            line = line.strip()
            if line:
                total += int(line)
        print(total)
except FileNotFoundError:
    print("Ошибка: Файл не найден")


"""13"""
import datetime
with open("log.txt.py", "a+") as f:
    print(f.write(datetime.datetime.now().strftime("\n%d.%m.%Y %H:%M:%S")))

