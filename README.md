# Python Quiz

Python으로 만든 콘솔 기반 수도 퀴즈 게임입니다.

## 기능

- 퀴즈 풀기
- 퀴즈 추가/삭제
- 힌트 보기(힌트 1회당 10점 감점)
- 최고 점수 확인
- 플레이 기록 확인

## 실행 방법

```bash
git clone https://github.com/Beda28/2.Quiz.git
cd 2.Quiz
python main.py
```

## 메뉴

```text
1. 퀴즈 시작
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 퀴즈 삭제
6. 게임 기록
7. 게임 종료
```

## 저장 방식

게임 상태는 `state.json`에 저장됩니다.

- `quizzes`:    퀴즈 목록
- `best_score`: 최고 점수
- `history`:    플레이 기록

상태 파일이 없거나 문제가 있으면 기본 퀴즈로 다시 시작됩니다.

## 참고 문서

- [docs/history.md](docs/history.md)
- [docs/git.md](docs/git.md)