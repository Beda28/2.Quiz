def read_int(prompt):
    input_value = int(input(prompt))

    if input_value < 0:
        return ("음수는 입력할 수 없습니다.")
    return input_value

def read_str(prompt):
    input_value = input(prompt)

    if input_value.strip() == "":
        return ("빈 문자열은 입력할 수 없습니다.")
    return input_value