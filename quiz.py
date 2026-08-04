from input import read_int
# from default_quiz import DEFAULT_QUIZZES
# from storage import loadstate

import os
import time

def question(quizzes):
    score = 0

    for quiz in quizzes:
        os.system("cls")
        print(quiz["title"])
        choices(quiz["choices"])
        if answer(quiz["answer"]):
            score += 1
        time.sleep(1)

    return score, len(quizzes)

def choices(choice_list: dict):
    for number, content in choice_list.items():
        print(f"{number}. {content}")

def answer(correct_answer: int):
    user_answer = read_int("정답을 입력해주세요 : ")

    if user_answer == correct_answer:
        print("정답입니다!")
        return True
    else:
        print(f"틀렸습니다. 정답은 {correct_answer}번입니다.")
        return False