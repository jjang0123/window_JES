from random import *

# 어휘 리스트
words = ["apple", "banana", "orange", "grape", "kiwi", "mango", "peach", "pear", "plum", "strawberry"]

while True:
    word = choice(words)  # 랜덤으로 단어 1개 선택
    letters = ""  # 입력한 글자 저장
    chances = 10  # 기회 10회 제한

    while True:
        succeed = True  # 성공 여부 확인 변수

        # 글자 수 만큼 밑줄/글자 출력
        for w in word:
            if w in letters:
                print(w, end=" ")
            else:
                print("_", end=" ")
                succeed = False
        print()

        # 성공
        if succeed:
            print("Good Job!")  # 성공 문구
            break

        # 실패
        if chances <= 0:
            print("Fail!")  # 실패 문구
            print(f"The word was: {word}")
            break

        # 글자 입력받기
        letter = input("Input letter > ").strip()

        # 새로 입력받은 글자 추가
        if letter not in letters:
            letters += letter

        # 단어 포함 여부 판별
        if letter in word:
            print("Correct")
        else:
            chances -= 1  # 기회 차감
            print(f"Nope! {chances} trials left")

    # 게임 재진행 여부 선택
    retry = input("\n게임을 계속하시겠습니까? (y/n): ").strip().lower()
    if retry != 'y':
        print("게임을 종료합니다.")
        break