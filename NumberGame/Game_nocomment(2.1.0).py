#     << 절차적 프로그래밍 >>
# [ 게임 의사 코드 작성 및 설계 ]

game_txt = [
    '나는 휘니야 \n반가워~', 
    'v2.1.0', '어서와~ 너의 이름을 알려줘~\n', '이 이름은 안되 미안하지만, 다시~',
    '다시 게임을 할까?(Yes/No) 대소문자 관계 없어~\n',
    '정확하게 (Yes/No)로 입력해줘~\n(응, 아니)는 안돼 능력 밖이야',
    'Game over !! Bye Bye~ See U Soon '
]

game_txtEx = {
    'GAME_INTROW':
    '''
    자~{name} 게임을 시작해볼까?
    숫자는 내가 무작위로 정했어 
    ''',
    'GAME_INTRO':
    '''
    %s0 ~ 50사이의 숫자를 넣어봐~ \n
    ''',
    'INPUT_EMPTY':
    '값이 정확 하지 않아; 다시 확인 해줄래?',
    'INPUT_NOT_NUM':
    '숫자가 아닌걸??',
    'out_of_bound':
    '응? 숫자가 0~50사이가 아닌데?\n0~50 사이로 다시 부탁해~',
    'check_err01':
    '''
    {name}...너의 숫자가 많아..
    {name}의 지금까지 도전 횟수는 {cnt}번이야.
    ''',
    'check_err02':
    '''
    {name}...너의 숫자가 부족해....
    {name}의 지금까지 도전 횟수는 {cnt}번이야.
    ''',
    'check_success':
    '''
         {name}:{0} = 휘니:{1} 
    우왕! 맞았어! 내가 생각한 숫자야!
       대단해 ~ 아주 아주 칭찬해 ~
    {name}의 총 도전 횟수는 {cnt}번이야.
       너의 점수는 {score}점이야~!!
    '''
}

game_title = "UP AnD DoWN"
cell_amt = 40
form = '={0:^%s}=' % (cell_amt - 2)

print('=' * cell_amt)
print(form.format(game_title))
print(form.format(game_txt[1]))
print('=' * cell_amt)

nameCheck = True
while nameCheck:
    gamer_name = input(game_txt[2]).strip()
    if not gamer_name:
        print(game_txt[3])
        continue
    nameCheck = False
# print('----------------')
print('-' * cell_amt)
print(game_txt[0], gamer_name)

game_run = True
while game_run:
    ai_num = None
    try_count = 0
    # print('----------------')
    print('-' * cell_amt)

    print(game_txtEx['GAME_INTROW'].format(name=gamer_name))
    # print('----------------')

    while True:
        while True:
            # print(gamer_name)
            gamer_num = input(game_txtEx['GAME_INTRO'] %gamer_name).strip()

            if not gamer_num:
                print(game_txtEx['INPUT_EMPTY'])
                continue

            elif not gamer_num.isnumeric():
                print(game_txtEx['INPUT_NOT_NUM'])
                continue

            gamer_num = int(gamer_num)
            if gamer_num < 0 or gamer_num > 51:
                print(game_txtEx['out_of_bound'])
                continue
            break

        import random

        if not ai_num:
            ai_num = random.randint(1, 51)
            # print('ai_num=', ai_num)

        try_count += 1

        if gamer_num > ai_num:
            print(game_txtEx['check_err01'].format(
                ai_num,
                gamer_num,
                score=(110 - try_count * 10),
                cnt=try_count,
                name=gamer_name))
        elif gamer_num < ai_num:
            print(game_txtEx['check_err02'].format(
                ai_num,
                gamer_num,
                score=(110 - try_count * 10),
                cnt=try_count,
                name=gamer_name))
        else:
            print(game_txtEx['check_success'].format(
                gamer_num,
                ai_num,
                score=(110 - try_count * 10),
                cnt=try_count,
                name=gamer_name))
            break

    while True:
        ans = input(game_txt[4]).strip().upper()
        if ans == 'YES':
            break
        elif ans == 'NO':
            print(game_txt[6])
            game_run = False
            break
        else:
            print(game_txt[5])

import sys
sys.exit()
