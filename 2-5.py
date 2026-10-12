year=int(input("년도를 입력하세요: "))
if year % 400 == 0:
    print(f"{year}은 윤년입니다.")
elif year % 100 == 0:
    print(f"{year}은 평년입니다.")
elif year % 4 == 0:
    print(f"{year}은 윤년입니다.")
else:
    print(f"{year}은 평년입니다.")