# 파일명 입력
filename = input("파일 이름을 입력하세요: ")

# 내용 읽기
try:
    file = open(filename, "r")
    content = file.read()
    file.close()

    # 글자 수 세기
    characters = len("".join(content.split()))
    # 단어 수 세기
    words = len(content.split())
    # 줄 수 세기
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    print("characters :", characters)
    print("words      :", words)
    print("lines      :", len(lines))

except FileNotFoundError:
    print("파일이 존재하지 않습니다.")