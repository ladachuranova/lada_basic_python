"""1"""
def greet(name):
    print(f"Привет {name}! Добро пожаловать")
greet("Анна")


"""2"""
def square(num):
    print( num ** 2)
square(5)


"""3"""
def is_even(num):
    if num % 2 == 0:
        print( True)
    else:
        print(False)
is_even(4)
is_even(7)


"""4"""
def repeat_string(text, times):
    m = text * times
    print(m)
repeat_string("Python" ,3)


"""5"""
def add_max(a, b):
    res = a + b
    print(res)
add_max(3, 7)


"""6"""
def get_max(a, b, c):
    if a > b:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)
get_max(10, 25, 7)


"""7"""
def calculate(a, b, operation):
    if operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "*":
        print(a * b)
    elif operation == "/":
        print(a / b)
calculate(10, 5, "+")
calculate(10, 5, "*")


"""8"""
def reverse_ctrings(text):
    res = text[::-1]
    print(res)
reverse_ctrings("Python")


"""9"""
def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_spaces:
        s1 = s1.strip()
        s2 = s2.strip()
    if ignore_case:
        s1 = s1.lower()
        s2 = s2.lower()
    return s1 == s2
print(compare_strings("Hello", " hello "))  # True
print(compare_strings("Hello", "HELLO", ignore_case=False))  # False
print(compare_strings("Hello ", "Hello", ignore_spaces=False))  # False


"""10"""
def summarize(*args):
    return sum(arg for arg in args if isinstance(arg, (int, float)))
print(summarize(1, 2, 3))
print(summarize(10, "abc", 5, 2))


"""11"""
def create_profile(name, age, **extra):
    print("Профиль пользователя:")
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    if extra:
        print("Дополнительная информация:")
        for key, value in extra.items():
            print(f"{key}: {value}")
create_profile("Иван", 30, city="Москва", job="Инженер")


"""12"""
def process_orders(*orders, discount=0):
    ord = sum(orders)
    sale = 1 - (discount / 100)
    print(f"Сумма заказа: {ord}")
    print(f"С учетом скидки: {ord * sale}")
process_orders(100, 200, 300, discount=10)


"""13"""
def merge_lists(*lists):
    return [item for lst in lists for item in lst]
print(merge_lists([1, 2], [3, 4], [5, 6]))


"""14"""
def merge_dicts(*dicts):
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))
