# 절차적 프로그래밍
game_txt = [
    '게임 제목을 입력하시오\n',
    '아무것도 입력하지 않았습니다. 다시!!\n',
    '입력하신 "%s" 게임 제목은 최대 20자(현재 %s자 입력)를 초과할수 없습니다. 다시 입력하세요..\n'
    ,'v1.0.0'
    ,'게이머의 이름을 입력하세요?\n'
    ,'이름이 입력되지 않았습니다. 다시~'
    ,'다시 게임을 할까요?(yes/no) 대소문자 관계 없이 입력\n'
    ,'정확하게 (yes/no)로 입력하세요'
    ,'game over !! bye bye~'
    
]
game_txtEx = {
    'GAME_INTRO':"0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요",
    'INPUT_EMPTY':'값을 정확하기 입력하세요',
    'INPUT_NOT_NUM':'숫자가 아닙니다',
    'out_of_bound':'값이 범위를 넘어었습니다. 0~99 사이로 다시 입력',
    'check_err01':'값이 크다',
    'check_err02':'값이 작다',
    'check_success':'''
    정답입니다. 게이머:{0}, AI:{1}
                {name}님의 총 시도 횟수는 {cnt}회 입니다.
                획득 점수는 {score}점 입니다.
    '''


}
while True:
    game_title = input( game_txt[0] )
    if not game_title:
        print( game_txt[1] )        
    elif len(game_title) > 20:
        print( game_txt[2] % (game_title, len(game_title)) )        
    else:        
        break
print ( '[%s]'% game_title )

cell_amt = 40
form = '={0:^%s}=' % (cell_amt-2)
print('='*cell_amt)
print(form.format(game_title))
print(form.format(game_txt[3]))
print('='*cell_amt)

nameCheck = True
while nameCheck:
    gamer_name = input(game_txt[4])
    if not gamer_name:
        print( game_txt[5] )        
        continue    
    nameCheck = False
print( '정상입력', gamer_name  )

game_run = True
while game_run:
    ai_num = None
    try_count = 0
    while True:
        while True:
            gamer_num = input( game_txtEx['GAME_INTRO'] ).strip()
            if not gamer_num:
                print(game_txtEx['INPUT_EMPTY'] )
                continue
            elif not gamer_num.isnumeric():
                print(game_txtEx['INPUT_NOT_NUM'] )
                continue
            gamer_num = int(gamer_num)
            if gamer_num<0 or gamer_num>99:
                print(game_txtEx['out_of_bound'] )
                continue    
            break

        import random
        if not ai_num:
            ai_num = random.randint(0,99)
            print( 'ai_num=', ai_num)
        
        try_count +=1
        if gamer_num > ai_num:
            print(game_txtEx['check_err01'])
        elif gamer_num < ai_num:
            print(game_txtEx['check_err02'])
        else:
            print(game_txtEx['check_success'].format(
                gamer_num,
                ai_num,
                score=(100-try_count*10),
                cnt=try_count,
                name=gamer_name
            ) )
            break

    while True:
        ans = input( game_txt[6] ).strip().upper()
        if ans == 'YES':
            break
        elif ans == 'NO':
            print( game_txt[8] )
            # 전체 게임 종료
            game_run = False
            break            
        else: # 공백, 다른문자등 입력시, 잘못된 입력 전체
            print( game_txt[7] )

import sys
# 프로세스 종료
sys.exit()

