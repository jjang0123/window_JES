# 함수 정의
def min_max(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    return (min_val, max_val)

# 정수 입력
user_input = input("정수를 공백으로 구분하여 입력하세요: ")

# 입력받은 문자열을 정수 리스트로 변환
numbers_list = list(map(int, user_input.split()))

minimum, maximum = min_max(numbers_list)

# 출력
print(f"최솟값(min): {minimum}")
print(f"최댓값(max): {maximum}")