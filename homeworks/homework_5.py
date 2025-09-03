"""1"""
cities = [ "Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, 2, 3.4, "Cat", True]


"""2"""
print(numbers[-1])
#print(cities[10]) ошбка


"""3"""
numbers[1] = 10
print(numbers)
mixed[-1] = "Python"
print(mixed)


"""4"""
print(len(numbers))
print(sum(numbers))
print(sorted(numbers))


"""5"""
x = [1, 2, 3]
y = [4, 5]
print(x + y)

lst = ["Python", "is", "awesome"]
print(lst * 3)


"""6"""
print(3 in numbers)
print( "Москва" in cities)
print([1,2] in mixed)


"""7"""
numbers = [1, 2, 3, 4, 5]
numbers.remove(2)
print(numbers)

del cities[-1]
print(cities)


"""8"""
s = ["Python"]
print(list(s))
print(max(s))
print(min(s))
#print(sum(s)) ошибка



"""1"""
citi = ["Москва", "Вологда", "Череповец", "Иваново"]
citi2 = citi[:]
print(citi2)
print(id(citi))
print(id(citi2))


"""2"""
print(citi[1:2])
print(citi[2::])
print(citi[0::])
print(citi[-2::])


"""3"""
print(citi[0:2])
print(citi[-1])
print(citi[::-2])


"""4"""
citi[1:2] = "Сочи", "Нижний Новгород"
print(citi)
for i in range(1, len(citi), 2):
    citi[i] = "Город"
print(citi)

citi_1 = ["Москва", "Вологда", "Череповец", "Иваново"]
citi_1.append( "Волгоград")
citi_1.append("Омск")
print(citi_1)


"""5"""
x1 = [1, 2, 3]
y1 = [4, 5, 6]
print(x1 + y1)
s2 = ["Python", "rocks"]
print(s2 * 2)


"""6"""
print( [1, 2, 3] == [1, 2, 3])
print([10, 5, 3] > [5, 10, 3])
print([1, 2, 3] == [1, 2, "abc"])


"""7"""
chars = list("Python")
print(max(chars))
print(min(chars))
#print(sum(chars)) ошибка



"""1"""
numbers = [5, 10, 15]
numbers.append(20)
print(numbers)
numbers.insert(1,7)
print(numbers)
numbers.append("Python")
print(numbers)


"""2"""
del numbers[2]
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
numbers.clear()
print(numbers)


"""3"""
letters = ["a", "b", "c"]
print(id(letters))
l = letters.copy()
print(id(l))
ls = list(letters)
print(id(ls))


"""4"""
marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3))
print(marks.index(5))
# print(marks.index(6)) нет


"""5"""
nums = [8, 2, 5, 1, 7]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)


"""6"""
sities_2 = ["Москва", "Вологда", "Череповец", "Иваново"]
sities_2.sort()
print(sities_2)
st = sities_2.copy()
sorted(st)
print(st)


"""7"""
chars = list("programming")
print(chars.count("g"))
chars.reverse()
print(chars)
chars.sort()
print(chars)



"""1"""
matrix = [
    [1, 2, 3,4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix)
print(matrix[1])
print(matrix[2][0])


"""2"""
matrix[0] = 0
print(matrix)
matrix[1][-1] = "Python"
print(matrix)