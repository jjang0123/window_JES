while True:
    filename = input("파일명을 입력하세요: ")

    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        numbered_lines = []

        for i in range(len(lines)):
            new_line = str(i + 1) + " " + lines[i]
            numbered_lines.append(new_line)

        if "." in filename:
            dot_index = filename.rfind(".")
            save_filename = filename[:dot_index] + ".sav"
        else:
            save_filename = filename + ".sav"

        file = open(save_filename, "w")
        file.writelines(numbered_lines)
        file.close()

        print(save_filename, "파일로 저장했습니다.")
        break

    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")
        retry = input("다시 입력하시겠습니까? (y/n): ")

        if retry != "y":
            print("프로그램을 종료합니다.")
            break