from input import read_int

class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question
        self.choices  = choices
        self.answer   = answer
        self.hint     = hint

    @classmethod
    def from_dict(cls, quiz_data):
        return cls(
            quiz_data["question"],
            quiz_data["choices"],
            quiz_data["answer"],
            quiz_data.get("hint", "")
        )

    def to_dict(self):
        return {
            "question" : self.question,
            "choices"  : self.choices,
            "answer"   : self.answer,
            "hint"     : self.hint,
        }

    def show_quiz(self):
        print(self.question)
        print("0. 힌트 보기")

        for number, content in self.choices.items():
            print(f"{number}. {content}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

    def play(self):
        hint_used = False
        max_choice = len(self.choices)

        self.show_quiz()

        while True:
            user_answer = read_int("정답을 입력해주세요 : ", 0, max_choice)

            if user_answer == 0:
                if hint_used: print("이미 힌트를 사용했습니다.")
                else:
                    print(f"힌트: {self.hint if self.hint else '등록된 힌트가 없습니다.'}")
                    hint_used = True
                continue

            if self.check_answer(user_answer):
                print("정답입니다!")
                return True, hint_used

            print(f"틀렸습니다. 정답은 {self.answer}번입니다.")
            return False, hint_used