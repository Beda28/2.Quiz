import os
import random
import time

from datetime import datetime
from input    import read_int, read_str
from quiz     import Quiz
from storage  import loadstate, savestate

class QuizGame:
    def __init__(self):
        self.state   = loadstate()
        self.running = True

    def run(self):
        while self.running:
            self.clear_screen()
            self.show_menu()
            choice = read_int("선택지를 입력해주세요 : ", 1, 6)

            if   choice == 1: self.play_quiz()
            elif choice == 2: self.add_quiz()
            elif choice == 3: self.show_quiz_list()
            elif choice == 4: self.show_score()
            elif choice == 5: self.delete_quiz()
            elif choice == 6: self.exit_game()
            else:
                print("잘못된 선택입니다. 다시 시도해주세요.")
                time.sleep(1)

    def show_menu(self):
        print("어서오세요! 이곳은 퀴즈게임 !")
        print("다음 선택지 중 하나를 골라 게임을 시작하세요 !")
        print("1. 퀴즈 시작")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수/게임 기록 확인")
        print("5. 퀴즈 삭제")
        print("6. 게임 종료")

    def add_quiz(self):
        self.clear_screen()
        title      = read_str("퀴즈 제목을 입력해주세요 : ")
        choice_len = read_int("선택지 개수를 입력해주세요 (2 ~ 10) : ", 2, 10)
        choices    = {}

        for index in range(1, choice_len + 1):
            choices[index] = read_str(f"선택지 {index}: ")

        answer = read_int(f"정답 번호를 입력해주세요 (1 ~ {choice_len}) : ", 1, choice_len)
        hint   = read_str("힌트를 입력해주세요 : ")

        quiz = Quiz(title, choices, answer, hint)

        self.state["quizzes"].append(quiz.to_dict())
        if savestate(self.state):
            input("퀴즈가 성공적으로 추가되었습니다. 메뉴로 돌아가려면 Enter를 누르세요...")

    def play_quiz(self):
        if not self.state["quizzes"]:
            input("등록된 퀴즈가 없습니다. Enter를 누르세요...")
            return

        quizzes          = [Quiz.from_dict(quiz) for quiz in self.state["quizzes"]]
        random.shuffle(quizzes)
        quiz_count       = read_int(f"몇 문제를 풀까요? (1~{len(quizzes)}): ", 1, len(quizzes))
        selected_quizzes = quizzes[:quiz_count]
        correct_count    = 0
        hint_count       = 0

        for quiz in selected_quizzes:
            self.clear_screen()
            is_correct, hint_used = quiz.play()

            if is_correct:
                correct_count += 1

            if hint_used:
                hint_count += 1

            time.sleep(1)

        total       = len(selected_quizzes)
        raw_score   = correct_count / total * 100
        final_score = max(raw_score - hint_count * 10, 0)

        best_score  = self.state.get("best_score", 0)
        is_new_best = final_score > best_score

        if is_new_best:
            self.state["best_score"]   = final_score
            self.state["best_correct"] = correct_count
            self.state["best_total"]   = total

        history = self.state.setdefault("history", [])
        history.append({
            "played_at":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total":      total,
            "correct":    correct_count,
            "hint_count": hint_count,
            "score":      round(final_score, 2),
        })

        savestate(self.state)
        self.clear_screen()

        print("최종 결과")
        print(f"맞춘 문제 수: {correct_count}/{total}")
        print(f"점수: {final_score:.2f}점")
        print(f"힌트 사용: {hint_count}회")
        
        if is_new_best: print("축하합니다! 새로운 최고 점수를 달성했습니다!")
        else:           print(f"최고 점수: {best_score:.2f}점")
        input("\n메뉴로 돌아가려면 Enter를 누르세요...")

    def show_quiz_list(self):
        self.clear_screen()
        print("퀴즈 목록은 다음과 같습니다 !\n")

        for quiz_number, quiz_data in enumerate(self.state["quizzes"], start=1):
            quiz = Quiz.from_dict(quiz_data)
            print(f"{quiz_number}. {quiz.title}")

        input ("\n메뉴로 돌아가려면 Enter를 누르세요...")

    def delete_quiz(self):
        self.clear_screen()
        quizzes = self.state.get("quizzes", [])

        if not quizzes:
            input("삭제할 퀴즈가 없습니다. Enter를 누르세요...")
            return

        print("삭제할 퀴즈를 선택해주세요.\n")
        print("0. 취소")

        for index, quiz_data in enumerate(quizzes, start=1):
            quiz = Quiz.from_dict(quiz_data)
            print(f"{index}. {quiz.title}")

        delete_number = read_int(f"\n삭제할 퀴즈 번호를 입력해주세요 (0~{len(quizzes)}): ", 0, len(quizzes))

        if delete_number == 0:
            input("퀴즈 삭제를 취소했습니다. 메뉴로 돌아가려면 Enter를 누르세요...")
            return

        deleted_quiz = Quiz.from_dict(quizzes.pop(delete_number - 1))

        if savestate(self.state):
            input(
                f"'{deleted_quiz.title}' 퀴즈를 삭제했습니다.\n"
                "메뉴로 돌아가려면 Enter를 누르세요..."
            )

    def show_score(self):
        self.clear_screen()
        best_score   = self.state.get("best_score", 0)
        best_total   = self.state.get("best_total", 0)
        best_correct = self.state.get("best_correct", 0)
        history      = self.state.get("history", [])

        if best_total == 0 and not history:
            input("저장된 점수나 게임 기록이 없습니다. Enter를 누르세요...")
            return

        print("최고 점수")
        print(f"최고 점수: {best_score:.2f}점")
        print(f"{best_total}문제 중 {best_correct}문제 정답")

        if history:
            print("게임 기록")

            for index, record in enumerate(history, start=1):
                print(
                    f"{index}. {record['played_at']} | "
                    f"{record['total']}문제 중 {record['correct']}문제 정답 | "
                    f"힌트 {record['hint_count']}회 | "
                    f"{record['score']:.2f}점"
                )

        input("\n메뉴로 돌아가려면 Enter를 누르세요...")

    def exit_game(self):
        savestate(self.state)
        self.running = False
        print("성공적으로 게임을 종료했습니다.")

    def clear_screen(self):
        os.system("clear")