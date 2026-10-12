# 모음 개수를 반환하는 함수
def count_vowel(text):
    vowels = "aeiouAEIOU"  # 영어 모음 (대소문자 포함)
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# 문자열 입력받기
user_text = input("문자열을 입력하세요: ")

result = count_vowel(user_text)

# 모음 개수 출력
print(f"입력한 문자열 속 모음의 개수: {result}")