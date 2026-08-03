from input import read_int

def question():
    quiz = {
        "title": "대한민국의 수도는 어디일까요?",
        "choices":{
            1: "서울",
            2: "부산",
            3: "대구",
            4: "인천"
        },
        "answer": 1
    }

    print(quiz["title"])
    choices(quiz["choices"])
    answer(quiz["answer"])
    
def choices(choice_list: dict):
    for number, content in choice_list.items():
        print(f"{number}. {content}")

def answer(correct_answer: int):
    user_answer = read_int("정답을 입력해주세요 : ")

    if user_answer == correct_answer:
        print("정답입니다!")
    else:
        print(f"틀렸습니다. 정답은 {correct_answer}번입니다.")