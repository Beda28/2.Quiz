# Git 사용 기록

이 문서는 Python 퀴즈 게임 프로젝트에서 Git을 사용하며 익힌 기본 흐름과 명령어를 정리한 문서입니다.

## 1. 브랜치 생성 및 전환

```bash
git checkout -b <브랜치이름>
```

```bash
PS [ 프로젝트 폴더 경로 ]> git checkout -b feature/quiz-game
Switched to a new branch 'feature/quiz-game'
```

## 2. 브랜치 확인

```bash
git branch
```
```bash
PS [ 프로젝트 폴더 경로 ]> git branch
* feature/score-percentage
  main
```

## 3. 업스트림 브랜치 설정 및 push

```bash
git push --set-upstream origin <브랜치이름>
```

```bash
PS [ 프로젝트 폴더 경로 ]> git push --set-upstream origin feature/quiz-add
```

## 4. 원격 저장소 복제

```bash
git clone <저장소 주소>
```

## 5. 원격 저장소에서 최신 변경사항 받기

```bash
git pull
```

## 6. 커밋 메시지 규칙

| 유형         | 설명                | 예시                         |
| ---------- | ----------------- | -------------------------- |
| `feat`     | 새로운 기능 추가         | `feat: 퀴즈 삭제 기능 추가`        |
| `fix`      | 오류 수정             | `fix: 퀴즈가 없을 때 실행 오류 수정`   |
| `refact`   | 기능 변경 없는 코드 구조 개선 | `refact: Quiz 클래스 구조 개선` |
| `docs`     | README 및 문서 수정    | `docs: 실행 방법 추가`           |
| `merge`    | 브랜치 병합            | `merge: 퀴즈 추가 기능 병합`       |

커밋 메시지는 `유형: 작업 내용` 형식으로 작성합니다.
