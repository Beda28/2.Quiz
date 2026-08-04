# 1. 문서 개요

```
본 문서는 파이썬을 통한 퀴즈게임 제작 과정을 담은 문서입니다.
파이썬 프로그래밍에 익숙해지는것을 목표로 합니다.
```

## 2. 퀴즈 주제 선정
```js
퀴즈 주제는 '포켓몬'으로 하였습니다.
유명한 ip인만큼, 문제로 출제할 수 있는 내용들이 많기 때문에 결정했습니다.
```

## 3. 기본 퀴즈
[ 기본 퀴즈 내용 ](default_quiz.py)

## 4. 구현된 기능

#### 기본 문제 영역
- 퀴즈 풀기
- 플레이기록 / 최고점수 확인
- 퀴즈 추가
- 힌트 보기(힌트 1회당 10점 감점)
- 게임 종료

#### 보너스 문제 영역
- 퀴즈 순서 랜덤 출제
- 문제 수 선택
- 힌트 기능
- 퀴즈 삭제 기능
- 점수 기록 히스토리 (상세기록)

## 5. 실행 방법

```bash
git clone https://github.com/Beda28/2.Quiz.git
cd 2.Quiz
python main.py
```

## 6. 저장 방식
[ state.json ](state.json)

## 7. 참고 문서
- [docs/history.md](docs/history.md)
- [docs/git.md](docs/git.md)

## 8. 인게임 스크린샷
### 퀴즈 메뉴
![ 메뉴 이미지 ](images/1.%20menu.png)
---
### 퀴즈 추가
![ 추가 이미지 ](images/2.%20add.png)
---
### 퀴즈 목록
![ 목록 이미지 ](images/3.%20list.png)
---
### 퀴즈 플레이
#### 문제 개수 선택
![ 문제 개수 선택 이미지 ](images/4.%20select.png)
---
#### 힌트 사용하지 않은 문제
![ 힌트 없는 문제 풀이 이미지 ](images/5.%20no_hint.png)
---
#### 힌트 사용한 문제
![ 힌트 사용한 문제 풀이 이미지 ](images/6.%20hint.png)
---
#### 최종 점수 공개
![ 최종 점수 공개 이미지 ](images/7.%20last.png)
---
### 퀴즈 게임 기록 / 최고 점수 확인
![ 퀴즈 게임 기록 확인 이미지 ](images/8.%20score.png)
---
### 퀴즈 삭제
#### 퀴즈 삭제
![ 퀴즈 삭제 이미지 ](images/9.%20remove.png)
---
#### 퀴즈 삭제 확인
![ 퀴즈 삭제 확인 이미지 ](images/10.%20check.png)
### 깃허브 그래프
#### 해당 문서 작성 시점을 기준으로 합니다.
```bash
PS [ 프로젝트 폴더 경로 ]> git log --oneline --graph
* eb850a1 (HEAD -> main, origin/main, origin/HEAD) fix: 퀴즈 클래스 구조 변경
* db93988 docs: 문서 작성
* 358047b feat: 퀴즈 게임 진행 기록
* 414842f feat: 퀴즈 힌트 기능 추가
* d9e6ca4 feat: 퀴즈 삭제 기능
* cac6d9c feat: 퀴즈 출제 문제 개수 지정
* 767b6d8 feat: 퀴즈 랜덤 출제
* 2c63bce refact: 퀴즈 클래스화
*   5333bd6 merge: 퀴즈 추가 기능
|\  
| * 9d3bec6 (origin/feature/quiz-add, feature/quiz-add) docs: 추가기능 기록
| * 9e680d2 feat: 퀴즈 추가 기능
|/  
* b0fb7dd refact: 입력 처리 함수 개선
* a85c0c5 docs: 최고점수 기능
*   2a6bd84 merge: 최고점수 확인
:
* eb850a1 (HEAD -> main, origin/main, origin/HEAD) fix: 퀴즈 클래스 구조 변경
* db93988 docs: 문서 작성
* 358047b feat: 퀴즈 게임 진행 기록
* 414842f feat: 퀴즈 힌트 기능 추가
* d9e6ca4 feat: 퀴즈 삭제 기능
* cac6d9c feat: 퀴즈 출제 문제 개수 지정
* 767b6d8 feat: 퀴즈 랜덤 출제
* 2c63bce refact: 퀴즈 클래스화
*   5333bd6 merge: 퀴즈 추가 기능
|\  
| * 9d3bec6 (origin/feature/quiz-add, feature/quiz-add) docs: 추가기능 기록
| * 9e680d2 feat: 퀴즈 추가 기능
|/  
* b0fb7dd refact: 입력 처리 함수 개선
* a85c0c5 docs: 최고점수 기능
*   2a6bd84 merge: 최고점수 확인
|\  
| * f8cdef4 (origin/feature/high-score, feature/high-score) feat: 최고점수 확인
| * d5d2f21 docs: 브랜치명 수정
* | af11975 docs: 브랜치명 수정
:
* eb850a1 (HEAD -> main, origin/main, origin/HEAD) fix: 퀴즈 클래스 구조 변경
* db93988 docs: 문서 작성
* 358047b feat: 퀴즈 게임 진행 기록
* 414842f feat: 퀴즈 힌트 기능 추가
* d9e6ca4 feat: 퀴즈 삭제 기능
* cac6d9c feat: 퀴즈 출제 문제 개수 지정
* 767b6d8 feat: 퀴즈 랜덤 출제
* 2c63bce refact: 퀴즈 클래스화
*   5333bd6 merge: 퀴즈 추가 기능
|\  
| * 9d3bec6 (origin/feature/quiz-add, feature/quiz-add) docs: 추가기능 기록
| * 9e680d2 feat: 퀴즈 추가 기능
|/  
* b0fb7dd refact: 입력 처리 함수 개선
* a85c0c5 docs: 최고점수 기능
*   2a6bd84 merge: 최고점수 확인
|\  
| * f8cdef4 (origin/feature/high-score, feature/high-score) feat: 최고점수 확인
| * d5d2f21 docs: 브랜치명 수정
* | af11975 docs: 브랜치명 수정
|/  
* 2aa7d69 (origin/feature/score-percentage, feature/score-percentage) docs: branch 병합
* 28f309c feat: 점수 퍼센트에이지 출력
* 0318abe docs: README 개편 및 개발기록 분리
* b5e5059 feat: 퀴즈게임 실행 및 점수관리
* efc338e feat: 파일 저장 및 불러오기
* 5db2c4d feat: 기본 퀴즈 데이터 추가
* fe8b0d7 feat: 퀴즈 메인로직 제작
:
* eb850a1 (HEAD -> main, origin/main, origin/HEAD) fix: 퀴즈 클래스 구조 변경
* db93988 docs: 문서 작성
* 358047b feat: 퀴즈 게임 진행 기록
* 414842f feat: 퀴즈 힌트 기능 추가
* d9e6ca4 feat: 퀴즈 삭제 기능
* cac6d9c feat: 퀴즈 출제 문제 개수 지정
* 767b6d8 feat: 퀴즈 랜덤 출제
* 2c63bce refact: 퀴즈 클래스화
*   5333bd6 merge: 퀴즈 추가 기능
|\  
| * 9d3bec6 (origin/feature/quiz-add, feature/quiz-add) docs: 추가기능 기록
| * 9e680d2 feat: 퀴즈 추가 기능
|/  
* b0fb7dd refact: 입력 처리 함수 개선
* a85c0c5 docs: 최고점수 기능
*   2a6bd84 merge: 최고점수 확인
|\  
| * f8cdef4 (origin/feature/high-score, feature/high-score) feat: 최고점수 확인
| * d5d2f21 docs: 브랜치명 수정
* | af11975 docs: 브랜치명 수정
|/  
* 2aa7d69 (origin/feature/score-percentage, feature/score-percentage) docs: branch 병합
* 28f309c feat: 점수 퍼센트에이지 출력
* 0318abe docs: README 개편 및 개발기록 분리
* b5e5059 feat: 퀴즈게임 실행 및 점수관리
* efc338e feat: 파일 저장 및 불러오기
* 5db2c4d feat: 기본 퀴즈 데이터 추가
* fe8b0d7 feat: 퀴즈 메인로직 제작
* 75c5d7f feat: 공통 입력 처리 구현
:
* eb850a1 (HEAD -> main, origin/main, origin/HEAD) fix: 퀴즈 클래스 구조 변경
* db93988 docs: 문서 작성
* 358047b feat: 퀴즈 게임 진행 기록
* 414842f feat: 퀴즈 힌트 기능 추가
* d9e6ca4 feat: 퀴즈 삭제 기능
* cac6d9c feat: 퀴즈 출제 문제 개수 지정
* 767b6d8 feat: 퀴즈 랜덤 출제
* 2c63bce refact: 퀴즈 클래스화
*   5333bd6 merge: 퀴즈 추가 기능
|\  
| * 9d3bec6 (origin/feature/quiz-add, feature/quiz-add) docs: 추가기능 기록
| * 9e680d2 feat: 퀴즈 추가 기능
|/  
* b0fb7dd refact: 입력 처리 함수 개선
* a85c0c5 docs: 최고점수 기능
*   2a6bd84 merge: 최고점수 확인
|\  
| * f8cdef4 (origin/feature/high-score, feature/high-score) feat: 최고점수 확인
| * d5d2f21 docs: 브랜치명 수정
* | af11975 docs: 브랜치명 수정
|/  
* 2aa7d69 (origin/feature/score-percentage, feature/score-percentage) docs: branch 병합
* 28f309c feat: 점수 퍼센트에이지 출력
* 0318abe docs: README 개편 및 개발기록 분리
* b5e5059 feat: 퀴즈게임 실행 및 점수관리
* efc338e feat: 파일 저장 및 불러오기
* 5db2c4d feat: 기본 퀴즈 데이터 추가
* fe8b0d7 feat: 퀴즈 메인로직 제작
* 75c5d7f feat: 공통 입력 처리 구현
* e55f064 feat: first commit
~
(END)
* eb850a1 (HEAD -> main, origin/main, origin/HEAD) fix: 퀴즈 클래스 구조 변경
* db93988 docs: 문서 작성
* 358047b feat: 퀴즈 게임 진행 기록
* 414842f feat: 퀴즈 힌트 기능 추가
* d9e6ca4 feat: 퀴즈 삭제 기능
* cac6d9c feat: 퀴즈 출제 문제 개수 지정
* 767b6d8 feat: 퀴즈 랜덤 출제
* 2c63bce refact: 퀴즈 클래스화
*   5333bd6 merge: 퀴즈 추가 기능
|\  
| * 9d3bec6 (origin/feature/quiz-add, feature/quiz-add) docs: 추가기능 기록
| * 9e680d2 feat: 퀴즈 추가 기능
|/  
* b0fb7dd refact: 입력 처리 함수 개선
* a85c0c5 docs: 최고점수 기능
*   2a6bd84 merge: 최고점수 확인
|\  
| * f8cdef4 (origin/feature/high-score, feature/high-score) feat: 최고점수 확인
| * d5d2f21 docs: 브랜치명 수정
* | af11975 docs: 브랜치명 수정
|/  
* 2aa7d69 (origin/feature/score-percentage, feature/score-percentage) docs: branch 병합
* 28f309c feat: 점수 퍼센트에이지 출력
* 0318abe docs: README 개편 및 개발기록 분리
* b5e5059 feat: 퀴즈게임 실행 및 점수관리
* efc338e feat: 파일 저장 및 불러오기
* 5db2c4d feat: 기본 퀴즈 데이터 추가
* fe8b0d7 feat: 퀴즈 메인로직 제작
* 75c5d7f feat: 공통 입력 처리 구현
* e55f064 feat: first commit
~
(END)
* eb850a1 (HEAD -> main, origin/main, origin/HEAD) fix: 퀴즈 클래스 구조 변경
* db93988 docs: 문서 작성
* 358047b feat: 퀴즈 게임 진행 기록
* 414842f feat: 퀴즈 힌트 기능 추가
* d9e6ca4 feat: 퀴즈 삭제 기능
* cac6d9c feat: 퀴즈 출제 문제 개수 지정
* 767b6d8 feat: 퀴즈 랜덤 출제
* 2c63bce refact: 퀴즈 클래스화
*   5333bd6 merge: 퀴즈 추가 기능
|\  
| * 9d3bec6 (origin/feature/quiz-add, feature/quiz-add) docs: 추가기능 기록
| * 9e680d2 feat: 퀴즈 추가 기능
|/  
* b0fb7dd refact: 입력 처리 함수 개선
* a85c0c5 docs: 최고점수 기능
*   2a6bd84 merge: 최고점수 확인
|\  
| * f8cdef4 (origin/feature/high-score, feature/high-score) feat: 최고점수 확인
| * d5d2f21 docs: 브랜치명 수정
* | af11975 docs: 브랜치명 수정
|/  
* 2aa7d69 (origin/feature/score-percentage, feature/score-percentage) docs: branch 병합
* 28f309c feat: 점수 퍼센트에이지 출력
* 0318abe docs: README 개편 및 개발기록 분리
* b5e5059 feat: 퀴즈게임 실행 및 점수관리
* efc338e feat: 파일 저장 및 불러오기
* 5db2c4d feat: 기본 퀴즈 데이터 추가
* fe8b0d7 feat: 퀴즈 메인로직 제작
* 75c5d7f feat: 공통 입력 처리 구현
* e55f064 feat: first commit