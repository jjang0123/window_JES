for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(f"{i}은 3의 배수입니다.")
    elif i % 5 == 0 and i % 3 != 0:
        print(f"{i}은 5의 배수입니다.")
    elif i % 3 == 0 and i % 5 == 0:
        print(f"{i}은 3과 5의 배수입니다.")