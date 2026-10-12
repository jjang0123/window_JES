while True:
    filename = input("파일명을 입력하세요: ")

    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        for i in range(len(lines)):
            print(i + 1, lines[i], end="")

        break

    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")
        retry = input("다시 입력하시겠습니까? (y/n): ")

        if retry != "y":
            print("프로그램을 종료합니다.")
            break