from input import read_int
from default_quiz import DEFAULT_QUIZZES

import os
import time

def question():
    for quiz in DEFAULT_QUIZZES:
        os.system("cls")
        print(quiz["title"])
        choices(quiz["choices"])
        answer(quiz["answer"])
        time.sleep(1)

def choices(choice_list: dict):
    for number, content in choice_list.items():
        print(f"{number}. {content}")

def answer(correct_answer: int):
    user_answer = read_int("정답을 입력해주세요 : ")

    if user_answer == correct_answer:
        print("정답입니다!")
    else:
        print(f"틀렸습니다. 정답은 {correct_answer}번입니다.")