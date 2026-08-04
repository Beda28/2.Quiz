import os
import time

from input import read_int
from quiz import question
from storage import loadstate, savestate

class QuizGame:
    def __init__(self):
        self.state = loadstate()
        self.running = True

    def run(self):
        while self.running:
            self.clear_screen()
            self.show_menu()
            choice = read_int("선택지를 입력해주세요 : ")

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                pass  # 퀴즈 추가 기능은 아직 구현되지 않았습니다.
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.exit_game()
            else:
                print("잘못된 선택입니다. 다시 시도해주세요.")
                time.sleep(1)

    def show_menu(self):
        print("어서오세요! 이곳은 퀴즈게임 !")
        print("다음 선택지 중 하나를 골라 게임을 시작하세요 !")
        print("1. 퀴즈 시작")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 게임 종료")

    def play_quiz(self):
        quizzes = self.state["quizzes"]
        score, total = question(quizzes)

        best_score = self.state.get("beat_score")
        is_new_best = score / total * 100 > best_score
        if is_new_best:
            self.state["beat_score"] = score / total * 100
            self.state["best_correct"] = score
            self.state["best_total"] = total

        savestate(self.state)
        self.clear_screen()

        print("최종 결과")
        print(f"맞춘 문제 수: {score}/{total}")
        print(f"점수: {score / total * 100:.0f}점")
        
        if is_new_best:
            print("축하합니다! 새로운 최고 점수를 달성했습니다!")
        else:
            print(f"최고 점수: {best_score:.0f}점")
        input("\n메뉴로 돌아가려면 Enter를 누르세요...")

    def show_quiz_list(self):
        self.clear_screen()
        print("퀴즈 목록은 다음과 같습니다 !\n")
        for quiz_number, quiz in enumerate(self.state["quizzes"], start=1):
            print(f"{quiz_number}. {quiz['title']}")
        input ("\n메뉴로 돌아가려면 Enter를 누르세요...")

    def show_score(self):
        self.clear_screen()
        print(f"최고 점수: {self.state['beat_score']:.0f}점")
        print(f"{self.state['best_total']}문제 중 {self.state['best_correct']}문제 정답")
        input("\n메뉴로 돌아가려면 Enter를 누르세요...")

    def exit_game(self):
        savestate(self.state)
        self.running = False
        print("성공적으로 게임을 종료했습니다.")

    def clear_screen(self):
        os.system("cls")