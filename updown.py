import random

random_number = random.randint(1, 100)

while True:
    get = int(input('숫자를 입력하세요: '))
    if get < 1 or get > 100:
        print('유효한 범위 내의 숫자를 입력하세요')
    else:
        break


while True:
    if random_number > get:
        print('업!')
    elif random_number < get:
        print('다운~')
    else:
        print('맞았습니다!')
        break
    get = int(input('숫자를 입력하세요: '))

print(input('다시 하시겠습니까? (y/n):'))
