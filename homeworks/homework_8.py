"""1"""
numbers = [123, 34, 56, 67, 88]
it_numbers = iter(numbers)
print(next(it_numbers))
print(next(it_numbers))
print(next(it_numbers))
print(next(it_numbers))
print(next(it_numbers))


"""2"""
st_word = "Мороженое"
it_st_word = iter(st_word)
print(next(it_st_word))
print(next(it_st_word))
print(next(it_st_word))
print(next(it_st_word))
print(next(it_st_word))
print(next(it_st_word))
print(next(it_st_word))
print(next(it_st_word))
print(next(it_st_word))


"""1"""
N = 10
result = [n ** 2 for n in range(1, N + 1)]
print(result)


"""2"""
num = [f"{n} четные числа" for n in range(-10, 10) if n % 2 == 0 ]
print(num)


"""3"""
word = ["кошка", "собака", "попугай", "хомяк"]
res_word = [len(w) for w in word]
print(res_word)


"""4"""
res_nums =[f"четное {n}" if n % 2 == 0  else f"нечетное {n}" for n in range(1, 20)]
print(res_nums)


"""5"""
list_word = [24, "Cat", [1,3]]
it_list_word = list(hasattr(obj, '__iter__') for obj in list_word)
print(it_list_word)
