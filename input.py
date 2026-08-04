def read_int(prompt, minimum, maximum):
    while True:
        try:
            value = input(prompt).strip()

            if value == "":
                print("빈 입력은 사용할 수 없습니다.")
                continue

            number = int(value)

            if not minimum <= number <= maximum:
                print(f"{minimum}~{maximum} 사이의 숫자를 입력해주세요.")
                continue

            return number

        except ValueError:
            print("숫자를 입력해주세요.")

def read_str(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("빈 문자열은 입력할 수 없습니다.")
            continue

        return value