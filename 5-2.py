def deco2_add(type):
    def decorator(func):
        def wrapper(a, b):
            result = func(a, b)
            if type == "math":
                return f"{a} + {b} = {result}"
            elif type == "word":
                return f"The sum of {a} and {b} is {result}"
            return result
        return wrapper
    return decorator


# 1. type = "math"
@deco2_add(type="math")
def add(a, b):
    return a + b

print(add(2, 4))


# 2. type = "word"
@deco2_add(type="word")
def add(a, b):
    return a + b

print(add(1, 2))