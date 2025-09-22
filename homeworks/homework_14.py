"""1"""
import math
print(math.sqrt(64))
print(math.pow(5, 3))


"""2"""
import random
n = random.randint(1, 10)
print(n)
r = random.choice(["Python", "Java", "C++"])
print(r)


"""3"""
from packege import my_module

print(my_module.add(3, 5))
print(my_module.multiply(4, 6))


"""4"""
"""В  package в ппке mains.py """


"""5"""
import time
start = time.time()
time.sleep(2)
end = time.time()
t = end - start
print(f"Код выполнялся {t:.4f} сек")


"""6"""
import requests
response = requests.get("https://api.github.com")
print(response.status_code)


"""7"""
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]
plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


"""8"""
