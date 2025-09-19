"""1"""
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res.upper()
    return wrapper
@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())


"""2"""
def repeat(n):
    def repeat_ini(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return repeat_ini
@repeat(3)
def hello():
    print("Hello!")
hello()


"""3"""
def cache(func):
    nn = {}
    def wrapper(*args):
        if args in nn:
            return nn[args]
        resl =func(*args)
        nn[args] = resl
        return resl
    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))
print(slow_add(2, 3))


"""4"""
import time
def timer(repeat):
    def timer_init(func):
        def wrapper(*args, **kwargs):
            for _ in range(repeat):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                print(f"Среднее время выполнения: {end_time - start_time}")
            return result
        return wrapper
    return timer_init
@timer(3)
def slow_function():
    time.sleep(1)
slow_function()