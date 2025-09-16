"""1"""
from homeworks.homework_5 import marks

set_1 = {1, 2, 3, 4, 5}
set_1.add(5)
print(set_1)


"""2"""
lst = ["Москва", "Вологда", "Череповец", "Новгород"]
set_2 = set(lst)
print(set_2)
print(len(set_2))


"""3"""
set_3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set_3.discard(5)
set_3.discard(15)
print(set_3)


"""4"""
lst_2 = "abrakadabra"
l = set(lst_2)
print(len(l))


"""5"""
set_4 = set()
set_4.update(  "hello", (1, 2, 3), [4, 5, 6])
set_4.add(10)
print(set_4)


"""6"""
a = {1, 2, 3, 4, 5 }
b = {1, 6, 7, 3, 5}
res_1 = a & b
print(res_1)
res_2 = a | b
print(res_2)
res_3 =a.difference(b)
print(res_3)
res_4 = b.difference(a)
print(res_4)
res_5 = a ^ b
print(res_5)


"""7"""
even_number = {2, 4, 6, 8, 10}
odd_numbers = {1, 3, 5, 7, 9}
res_6 =  even_number & odd_numbers #тут не будет пересечения
print(res_6)
res_7 = even_number | odd_numbers
print(res_7)


"""8"""
python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
result_1 = python_students & java_students
print(f"Записались на 2 курса {result_1}")
result_2 = python_students ^ java_students
print(f"Только один курс {result_2}")
result_3 = python_students | java_students
print(f"Хотя бы один курс {result_3}")


"""9"""
text1 = set("програмированние")
text2 = set("автоматизировать")
letters_1 = text1 & text2
print(f"Общие{letters_1}")
letters_2 = text1 | text2
print(f"Только в первом{letters_2}")
letters_3 = text1 ^ text2
print(f"Уникальные{letters_3}")



"""1"""
num = {x: x ** 2 for x in range(1,10)}
print(num)


"""2"""
words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
words2 = {x.upper() for x in words}
print(words2)


"""3"""
grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
grades1 = {name: ("отлично" if marks >= 80 else "удовлетворительно") for name, marks in grades.items()}
print(grades1)


"""4"""
text = {"Python", "automation", "programming", "testing"}
text3 = { x: len(x) for x in text}
print(text3)


"""5"""
n = 10
result_4 = {i: {x**2 for x in range(1, i+1)} for i in range(1, n+1)}
print(result_4)