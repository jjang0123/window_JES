def calc(*args, op='+'):
    # + 연산인 경우
    if op == '+':
        result = 0
        for num in args:
            result += num
        return result

    # * 연산인 경우
    elif op == '*':
        result = 1
        for num in args:
            result *= num
        return result

print(calc(1, 1, 4, op='+')) 
print(calc(1, 2, op='*'))