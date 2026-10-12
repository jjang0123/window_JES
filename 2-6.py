for n in range(2, 101):
    for i in range(2, n):
        if n % i == 0:
            break
    else:  
        print(f"{n}은 소수입니다")