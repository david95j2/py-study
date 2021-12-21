# python study
---
---
## 설치 및 라이브러리 (21.12.02)

1. Python Installation
- python 3.9.0
- Anaconda
  - jupyter notebook
  - tensorflow
  - spyder

2. Standard Lib
- Data type
- Operation
- Variables
- Containers
- Math
- Os and Sys
- File I/O
- Pickle

3. ide
- visual studio code

---
## 목적

- '케라스 창시자에게 배우는 딥러닝' 책 구현하기 


---
## 몇가지 지켜야 할 규칙
- 클래스의 이름은 대문자로 시작하고 뒤이어 소문자들로 작성해야 한다.
- 하나의 밑줄(_)로 시작하는 식별자(identifier)는 private인 식별자를 의미한다.
- 두개의 밑줄(__)로 시작하는 식별자는 강한 private인 식별자
- 파이썬은 스코프({})를 생략하고, 엄격한 코드라인 들여쓰기가 필요
- 문장의 맨 뒤에 '\'를 사용하게 되면 밑에 있는 줄과 이어지는 것을 의미
- 큰 따옴표 3개(""")를 3개씩 사용하면 여러줄에 걸쳐 문자열을 표현 

---
## 기초
- mutable : list, dict, numpy 등
- immutable : 숫자, 문자, tuple 등

- numpy 
  - Vevtor / matrix 생성
  - 행렬 곱 (dot product)
  - broadcast
  - index / slice / iterlator
  - concatenate
  - loadtxt(), rand(), argmax(), argmix(), ones(), zeros()


## Git Command

1. git add 취소하기
- $ git reset HEAD (파일명)
  - 없으면 파일 전체 취소

2. git commit 명 변경하기  
- $ git commit --amend

3. 로그확인
- $ git log

4. git commit 취소
- 로컬에서만 commit 했을때
  - $ git rest HEAD

---

## Error log

1. 2021.12.21 파이썬으로 파일 읽을때 절대경로를 그대로 같다 붙히면 나오는 에러
  >
  >  'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
  >
  - \ 를 ->  / 로 변경 후 열어야 오류 안뜸.