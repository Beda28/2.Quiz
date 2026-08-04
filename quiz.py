from input import read_int
# from default_quiz import DEFAULT_QUIZZES
# from storage import loadstate

import os
import time

class Quiz:
    def question(self, quizzes):
        score = 0

        for quiz in quizzes:
            self.show_quiz(quiz)
            if self.answer(quiz["answer"], len(quiz["choices"])):
                score += 1
            time.sleep(1)

        return score, len(quizzes)

    def show_quiz(self, quiz):
        os.system("cls")
        print(quiz["title"])
        self.choices(quiz["choices"])

    def choices(self, choice_list: dict):
        for number, content in choice_list.items():
            print(f"{number}. {content}")

    def answer(self, correct_answer: int, max_choice: int):
        user_answer = read_int("정답을 입력해주세요 : ", 1, max_choice)

        if user_answer == correct_answer:
            print("정답입니다!")
            return True
        else:
            print(f"틀렸습니다. 정답은 {correct_answer}번입니다.")
            return False