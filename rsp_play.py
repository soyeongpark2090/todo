import random


def check_winner(win_cnt, draw_cnt, lost_cnt):

    rsp = ['가위', '바위', '보']

    while True:
        computer_pick = random.choice(rsp)
        user_pick = input('가위, 바위, 보 중 하나를 선택하세요: ')
        if user_pick not in rsp:
            print('유효한 입력이 아닙니다')
            continue
            # continue조건 충족시, continue 하단의 코드가 더이상 실행되지 않고,
            # while문의 처음(=9행)으로 돌아감

        if user_pick == computer_pick:
            print('비겼어요!')
            draw_cnt += 1
        elif (user_pick == '가위' and computer_pick == '보') or (user_pick == '바위' and computer_pick == '가위') or (user_pick == '보' and computer_pick == '바위'):
            print('사용자 승리!')
            win_cnt += 1
            print(f'사용자: {user_pick}, 컴퓨터: {computer_pick}')
            break
        else:
            print('컴퓨터 승리!')
            lost_cnt += 1
        print(f'사용자: {user_pick}, 컴퓨터: {computer_pick}')
    return win_cnt, draw_cnt, lost_cnt


win_cnt = 0
draw_cnt = 0
lost_cnt = 0

while True:
    # check_winner() 삭제
    win_cnt, draw_cnt, lost_cnt = check_winner(win_cnt, draw_cnt, lost_cnt)
    restart = input('다시 시작하시겠습니까? (y/n): ')
    if restart == 'y':
        print('게임을 재시작합니다')
    elif restart == 'n':
        print('게임을 종료합니다')
        print(f'승:{win_cnt}, 무:{draw_cnt}, 패:{lost_cnt}')
        break
    else:
        break
