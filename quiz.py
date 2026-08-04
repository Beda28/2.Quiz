from input import read_int

import os
import time


class Quiz:
    def question(self, quizzes):
        correct_count = 0
        hint_count = 0

        for quiz in quizzes:
            self.show_quiz(quiz)

            is_correct, hint_used = self.answer(quiz)

            if is_correct:
                correct_count += 1

            if hint_used:
                hint_count += 1

            time.sleep(1)

        return correct_count, len(quizzes), hint_count

    def show_quiz(self, quiz):
        os.system("cls")
        print(quiz["title"])
        self.choices(quiz["choices"])

    def choices(self, choice_list: dict):
        print("0. 힌트 보기")
        for number, content in choice_list.items():
            print(f"{number}. {content}")

    def answer(self, quiz):
        hint_used = False
        max_choice = len(quiz["choices"])

        while True:
            user_answer = read_int("정답을 입력해주세요 : ", 0, max_choice)

            if user_answer == 0:
                if hint_used: print("이미 힌트를 사용했습니다.")
                else:
                    print(f"힌트: {quiz.get('hint', '등록된 힌트가 없습니다.')}")
                    hint_used = True
                continue

            if user_answer == quiz["answer"]:
                print("정답입니다!")
                return True, hint_used

            print(f"틀렸습니다. 정답은 {quiz['answer']}번입니다.")
            return False, hint_used

    def delete_quiz(self, quizzes):
        if not quizzes:
            return None

        print("삭제할 퀴즈를 선택해주세요.\n")
        print("0. 취소")
        for index, quiz in enumerate(quizzes, start=1):
            title = quiz.get("title", "제목 없음")
            print(f"{index}. {title}")

        delete_number = read_int(f"\n삭제할 퀴즈 번호를 입력해주세요 (0~{len(quizzes)}): ", 0, len(quizzes))
        if delete_number == 0:
            return None
        return quizzes.pop(delete_number - 1)