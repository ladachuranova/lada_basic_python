"""1"""
s = "Python"
print(s.upper())
print(s.lower())


"""2"""
msg = "абракадабра"
print(msg.count( "ра"))
print(msg.count("a", 2))
print(msg.count( "xyz"))


"""3"""
text = "абракадабра"
print(text.find("ка"))
print(text.rfind("а"))
print(text.find("xyz"))


"""4"""
text = "Я изучаю Java"
print( text.replace("Java", "Python"))
print(text.replace(" ", ""))



"""5"""
x = "Python"
print(x.isalpha())
num =  "12345"
print(num.isdigit())
g = "123abc"
print(g.isdigit())


"""6"""
code = "42"
print(code.zfill(5))
print(code.ljust(10, '*'))


"""7"""
fr = "яблоко, груша, банан"
print(fr.split(", "))
fr2 = "Python;Java;C++"
print(fr2.split(";"))


"""8"""
x = ["Привет", "мир", "!"]
print(' '.join(x))
f = ["apple", "banana", "cherry"]
print(','.join(f))


"""9"""
x = " Python"
print(x.strip())
x =  "Python "
print(x.lstrip())
x = " Python "
print(x.strip())


"""10"""
text = "программирование"
print(text.capitalize())
print(text.count("р"))
print(text.find("и"))
print(text[::-1])


"""1"""
text = "Hello\nPython"
print(text) # \n используется для переноса строки


"""2"""
t = "Python\tAutomation"
print(t) # простой пробел


"""3"""
path = "C:\new\test.txt"
path2 =  "C:\\new\\test.txt"
print(path2) # нужно добавить просто еще один \
x = "Марка вина \"Ягодка\""
print(x)


"""4"""
path3 = r"C:\new\test.txt"
print(path3) #есть буква r


"""5"""
s = "Hello\b World"
print(s)
s = "Hello\fPython"
print(s)


"""1"""
name = "Lada"
age = 20
text = f"Меня зовут {name}, мне {age} лет."
print(text)


"""2"""
text2 ="Меня зовут {0}, мне {1} лет.".format(name, age)
print(text2)


"""3"""
year = 2025
citi = "Москва"
text3 = f"Сегодня {year} год, и я живу в {citi}."
print(text3)
text4 = f"Через 5 лет будет {year + 5} год."
print(text4)


"""4"""
text5 = f"Дважды мой возраст: {age * 2}"
print(text5)


"""5"""
rate = 92.5
currency = "доллар"
text_format = "Курс валют: 1 {} = {} рубля.".format(currency, rate)
print(text_format)
num = 7
text_f = f"Квадрат числа {num} равен {num ** 2}."
print(text_f)

