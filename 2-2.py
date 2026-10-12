# 명단 작성
students = {}
while True:
    student_id = input("학번 입력(종료는 0): ")
    if student_id == "0": # 학번은 0 입력 시 종료
        break
    student_name = input("이름 입력(종료는 None): ")
    if student_name == "None": # 이름은 None 입력 시 종료
        break
    students[student_id] = student_name

print(students) # 만들어진 딕셔너리 출력

# 학번 조회
while True:
    find = input("학번을 입력하세요 ('quit' 입력 시 종료): ")

    # quit 입력 시 반복문 종료
    if find == "quit":
        print("프로그램을 종료합니다.")
        break

    if find in students:
        print(f"{find} 학번의 학생 이름은 {students[find]}입니다.")
    else:
        print("not found!")