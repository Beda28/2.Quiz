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

#### 작업 및 커밋 푸시

## 3. 브랜치 병합

```bash
git checkout main
git pull
git merge <브랜치이름>
git push origin main
```

```bash
PS [ 프로젝트 폴더 경로 ]> git checkout main
Switched to branch 'main'

PS [ 프로젝트 폴더 경로 ]> git pull
Already up to date.

PS [ 프로젝트 폴더 경로 ]> git merge feature/score-percentage
Updating abc1234..def5678
Fast-forward

PS [ 프로젝트 폴더 경로 ]> git push
```
