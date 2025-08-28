"""1"""
name = "Lada"
age = 20
height = 1.65
print(f"name: {name}, age: {age}, height: {height}")

"""2"""
x = 10
print(type(x))
x = 25,5
print(type(x))
x = "Python"
print(type(x))


"""3"""
a = 7
b = a
print(a)
a = 10
print(a)
print(b)


"""4"""
x = y = z = 100
print(x,y,z)
print(id(x))
print(id(y))
print(id(z))

x = 1
print(id(x))
y = 2
print(id(y))
z = 3
print(id(z))


"""5"""
a = 5
b = 10
a,b = b,a
print(a,b)

"""6"""
#Использование True, print, if как переменные это будет не правльно,
#потому что они используются для других дел)

"""7"""
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1))
print(type(var2))
print(type(var3))
var1 = "Python"
print(type(var1))


переменная = 10
print(переменная) # Работает, но лучше использовать англ язык
#для более лучшего понимания

name = "Alice"
age = 25
height = 1.69
citi = ["Moscow"]
print(type(name))
print(type(age))
print(type(height))
print(type(citi))