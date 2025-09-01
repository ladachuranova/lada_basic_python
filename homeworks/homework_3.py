"""1"""
a = "Привет, мир!"
b = 5, 10, 15
c = 10 + 25
print(a)
print(b)
print(c)


"""2"""
print(1, 2, 3, sep= " & ")

a = "Python"
b = "лучший язык"
print(a, b)


"""3"""
x = 3.14
y = -8
print(f"Координаты точки {x}, {y}")

n = input("ВВедите имя: ")
a = int(input("ВВудите возраст: "))
print(f"Имя: {n}, Возраст{a} ")


"""4"""
name = int("ИМЯ: ")
print(f"Привет {name}")


"""5"""
num1 = int(input("число1: "))
num2 = int(input("число2: "))
print(num1 + num2)




"""1"""
print(5 > 3)
print(10 < 2)
print(7 == 7)
print(6 != 8)
print(4 >= 4)
print(9 <= 3)
res = 8 > 12
print(type(res))


"""2"""
x = 15
print(x % 2 == 0)
print(x % 5 == 0)
print( x % 3 == 0 and x % 5 == 0)


"""3"""
у = 4.5
print(1 <= y <= 10)
print(0 <= y <= 5 or 10 <= y <= 15)
print(not y < 5)


"""4"""
print(True or False and False)
print(not False and True)
print(False or not True and True)
print(not (10 > 5 or 3 < 1))


"""5"""
print(bool(0))
print(bool(-5))
print(bool(3.14))
print(bool(""))
print(bool("Python"))
print(bool(" "))


"""6"""
n = 3
print(n > 0)
print(n % 3 == 0)



"""1"""
s = "Программирование"
print(s [0])
print(s [-1])
print(s[2],s[-2])

"""2"""
#print(s[100]) #Ошибка
print(len(s))


"""3"""
s = "Программирование"
print(s[:6])
print(s[-5::])
print(s[1:7])
print(s[::-1])


"""4"""
s = "Программирование"
print( s[0::3])
print(s[::-2])


"""5"""
#s[0] = "п" # ошибка
s2 = "п" + s[1:]
print(s2)


"""6"""
word = "abcdefgh"
print(word[2:5])
print(word[::-1])
print(word[1:-1])