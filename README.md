# 내배캠-Python 개인과제
AI부트_파이썬 활용 연습
<br><br>

## 🖥️ 개인과제 소개
* 파이썬을 활용하여 updown게임, rsp게임, 회원관리 프로그램, 그리고 rsp게임을 web상에서 구현했습니다.
<br><br>

## 🕰️ 개발 기간
* 24.02.22(목) - 24.02.29(목)
<br>

## 📌 주요 기능
### 과제1: updown game
* 터미널 상에서 사용자에게 질문에 대한 응답을 받고, 사용자와 컴퓨터가 updown게임을 할 수 있습니다.
* 게임은 유효범위 1~100까지 사이에서 이뤄지며, 유효범위를 벗어날 경우에는 유효하지 않은 입력이라는 문구와 함께 입력창이 다시 나타납니다.
* 플레이어가 게임을 계속 하고 싶을 때는 'y'를 입력해서 게임 재시작이 가능하고, 'n'를 입력시 게임이 종료됩니다.
* 게임 종료시에는 지금까지의 최고 시도 횟수가 표시됩니다.

### 과제2: rsp_game
* 터미널 상에서 사용자에게 sciss, rock, paper 중 하나에 대한 입력을 받고, 사용자와 컴퓨터가 rsp게임을 할 수 있습니다.
* 사용자와 컴퓨터가 선택할 수 있는 범위는 sciss, rock, paper이며, 이외의 입력은 유효하지 않다는 문구와 함께 입력창이 다시 나타납니다.
* 이 때 사용자가 입력하는 대소문자는 구분없이 모두 프로그램이 인식할 수 있습니다.
* 플레이어는 자신이 승리했을 경우에만 재시작 여부를 결정할 수 있으며, 그 외에는 계속해서 게임을 해야합니다.
* 게임 종료시에는 지금까지의 승무패 전적이 표시됩니다.(재시작한 경우에는 누적으로 표시됨)

### 과제3: 회원 및 게시물 관리
* 간단한 회원 관리 및 게시물 관리 프로그램입니다. 터미널 상에서 정보 입력을 받으며, 정보 입력이 끝나면 자동으로 등록된 회원 이름이 출력됩니다.
* 특정 유저가 작성한 게시물의 제목을 모아서 출력하고, 게시물 내용에 '민지'가 포함된 게시물의 제목을 출력합니다.

### 과제4: web에서 rsp_game하기
* 과제2를 활용하여 터미널 상이 아닌 web상에서 사용자의 입력을 받아 rsp game을 할 수 있습니다.
* 사용자와 컴퓨터의 게임 정보는 파이썬 database에 저장되며, database로부터 데이터를 받아와서 해당 web화면에 게임 결과 및 전적이 실시간으로 반영됩니다.
