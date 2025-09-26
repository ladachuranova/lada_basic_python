"""1"""
from collections.abc import mappingproxy

data = ["Python", 123, "Java", 456, "C++", 789]
def str_generator(lst):
    for item in lst:
        if isinstance(item, str):
            yield item
result = " ".join(str_generator(data))
print(result)


"""2"""
import random
def random_gen():
    for _ in range(10):
        yield random.randint(1, 100)
numbers = list(random_gen())
max_num = max(numbers)
print("Максимальное число:", max_num)


"""3"""
def long_words_generator(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for word in file.read().split():
            if len(word) > 5:
                yield word
result = " ".join(long_words_generator("words.txt"))
print(result)


"""4"""
def python_lines(data):
    with open(data, 'r', encoding='utf-8') as f:
        for data in f:
            if "Python" in data:
                yield data.rstrip()
for data in python_lines("text.txt"):
    print(data)


"""5"""
import random
def nums():
    while True:
        yield random.randint(1, 100)
for num in nums():
    print(num, end=' ')
    if num == 50:
        break


"""6"""
def prime_generator(N):
    count = 0
    num = 2
    while count < N:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1
print(" ".join(str(x) for x in prime_generator(10)))


"""7"""
def api_t():
    for i in range(1, 6):
        yield f"получение данных {i}"
gen = api_t()
for it in gen:
    print(it)


"""8"""
# input_user = input("Введите число ").split()
# num =list(map(lambda x: int(x)**2, input_user))
# print(num)


"""9"""
cities = ["Москва", "Санкт-Петербург", "Казань"]
cities_1 = list(map(str.upper, cities))
print(cities_1)


"""10"""
nums =  [15, 30, 45, 22, 60, 77, 90, 100]
even_num = filter(lambda x: x % 3 == 0 or x % 5 == 0, nums)
print(list(even_num))


"""11"""
lst = ["hello", "world42", "python3", "abc", "123", "data1science"]
lst_2 = list(filter(lambda x: any(char.isdigit() for char in x), lst))
print(lst_2)


"""12"""
countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
z = zip(countries, capitals)
print(dict(z))


"""13"""
data = [(1, 'a'), (2, 'b'), (3, 'c')]
z_1, z_2, = zip(*data)
print(z_1)
print(z_2)


"""14"""
names = ["петр", "Иван", "мария", "Анна"]
names.sort()
print(names)


"""15"""
products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]
print(sorted(products, reverse=True))
