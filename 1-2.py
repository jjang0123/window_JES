x = 10

def test():
    global x
    print(x)
    x = 20
# 출력
test()
print(x)