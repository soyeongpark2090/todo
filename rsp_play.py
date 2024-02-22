import random
rsp = ['가위', '바위', '보']
computer_random = random.choice(rsp)

while True:
    user_choice = input('가위, 바위, 보 중 하나를 선택하세요: ')
    if user_choice not in rsp:
        print('유효한 입력이 아닙니다')
        continue
    else:
        break

print(f'사용자: {user_choice}, 컴퓨터: {computer_random}')

while True:
    if user_choice == computer_random:
        print('비겼습니다!')
    elif (user_choice == rsp[0] and computer_random == rsp[2]) or (user_choice == rsp[1] and computer_random == rsp[0]) or (user_choice == rsp[2] and computer_random == rsp[1]):
        print('사용자 승리!')
    else:
        print('컴퓨터 승리!')
        break
print(input('다시 하시겠습니까? (y/n): '))
