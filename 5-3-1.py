def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def do_operation(func, x, y):
    return func(x, y)

result = do_operation(add, 2, 3)
print(result)