num = []                  # 1. 빈 리스트 생성

num.append(10)             # 2. 10 추가
num.append(20)
num.append(30)

num.insert(2, 40)          # 3. 20과 30 사이에 40 추가

del num[-1]               # 4. 마지막 요소 삭제
print(num)

print(sum(num))            # 5. 요소들의 합 출력