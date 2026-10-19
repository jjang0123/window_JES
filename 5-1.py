def deco_add(func):
    def wrapper(a, b):
        result = func(a, b)  # 원본 add 함수(a + b) 실행
        return f"{a} + {b} = {result}"  # 지정된 문자열 형식으로 반환
    return wrapper

@deco_add
def add(a,b):
    return a + b
print(add(2,4))
