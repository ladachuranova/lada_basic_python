"""1"""
from homeworks.homework_10 import words

num_1 = lambda x: x ** 2
print(num_1(3))


"""2"""
num_2 = lambda x: x % 2 == 0
print(num_2(4))
print(num_2(5))


"""3_1"""
sort_by_last_letter = sorted(words, key=lambda words: len(words[-1]))
words = ["banana", "apple", "cherry"]
print(sort_by_last_letter)

"""3_2"""
def sort_by_last_letter(words):
    return sorted(words, key=lambda x: x[-1])
words = ["banana", "apple", "cherry"]
print(sort_by_last_letter(words))


"""1"""
def multiply_by(n):
    def multiply_x(x):
        return n * x
    return multiply_x
times3 = multiply_by(3)
times5 = multiply_by(5)
print(times3(10))
print(times5(10))


"""2"""
def counter(start=0):
    value = start
    def counter_1():
        nonlocal value
        value += 1
        return value
    return counter_1
c1 = counter(5)
c2 = counter()
print(c1())
print(c1())
print(c2())
print(c2())