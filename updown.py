import random


def check_range():
    while True:
        get = int(input('숫자를 입력하세요: '))
        if get < 1 or get > 100:
            print('유효한 범위 내의 숫자를 입력하세요')
        else:
            return get


def generate_random():
    return random.randint(1, 100)


random_number = generate_random()
count = 0
count_list = []
best_point = 0

while True:
    get = check_range()
    if random_number > get:
        print('업!')
        count += 1
    elif random_number < get:
        print('다운~')
        count += 1
    else:
        print('맞았습니다!')
        print(f'시도한 횟수: {count}')
        count_list.append(count)
        print(count_list)
        # best_point = max(count_list)         # 방법1: max사용
        # ex. count_list = [5,8,6]         # 방법2: best_point로 변수 새롭게 선언
        for i in count_list:
            if i > best_point:
                best_point = i
        again = input('다시 하시겠습니까? (y/n):')
        if again != 'y':
            print(f'최고 시도 횟수는 {best_point}회입니다')
            break
        else:
            random_number = generate_random()
            count = 0
            print(f'게임을 재시작합니다')
            print(f'이전 게임의 최고 시도 횟수: {best_point}회')
