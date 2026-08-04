from quiz_game import QuizGame

def main():
    game = QuizGame()

    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다. 저장 후 종료합니다.")
        game.exit_game()

if __name__ == "__main__":
    main()