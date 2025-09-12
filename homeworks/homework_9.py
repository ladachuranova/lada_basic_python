"""1"""
fruits = {"Яблоко": 20, "Апельсин": 30, "Бананы": 40}
fruits.setdefault("Киви", 40)
print(fruits)


"""2"""
grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
for key, value in grades.items():
    if value >= 4:
        print(key)


"""3"""
cities = {"Италия":"Рим", "Япония": "Токио", "Франция":"Париж"}
title_c = input("Введите название страны: ")
print(cities.get(title_c, "Такой страны нету"))


"""4"""
students = [
    ("Анна", "Python"),
    ("Борис", "Java"),
    ("Виктор", "Python"),
    ("Галина", "C++"),
    ("Дмитрий", "Python")
]
print(dict(students))


"""5"""
students_2 = {"ST1": 3, "ST2":4, "ST3": 5, "ST4": 2, "ST5":3}
students_2.pop("ST4")
print(students_2)


"""6"""
students_3 = ["Анна", "Борис", "Виктор", "Галина"]
st = {st: None for st in students_3}
print(st)


"""7"""
exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
exchange_rates_n = input("Введите курс валюты: ")

rt = exchange_rates.get(exchange_rates_n, "Неизвестная валюта")
print(rt)
if exchange_rates_n not in exchange_rates:
   exchange_rates[exchange_rates_n] = None
print(exchange_rates)


"""8"""
dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
dict1.update(dict2)
print(dict1)



"""1"""
tapl_title = (1, 584, "Cat", ["fjif"], 758)
print(tapl_title[1])
print(tapl_title[-1])


"""2"""
nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
print(nums.count(4))
print(nums.index(7))


"""3"""
lst = ["Python", "Java", "C++", "JavaScript"]
lst_2 = tuple(lst)
print(lst_2)


"""4"""
cor = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(cor[0:3])
print(cor[-3::])
print(cor[0::2])


"""5"""
skj = (1, 3, ["Cat"], {"name": "Dog"})
skj[2][0] = "Python"
print(skj)
skj[3]["name"]= "JavaScript"
print(skj)