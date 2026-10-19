add = lambda a, b: a + b
sub = lambda a, b: a - b

def do_operation(func, x, y):
    return func(x, y)

result = do_operation(add, 2, 3)
print(result)  # 5

result = do_operation(sub, 2, 3)
print(result)  # -1