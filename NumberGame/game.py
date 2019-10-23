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
    # step 1-1 : 
    # 게임이 시작하면 다음의 프럼프트가 나온다 : "게임 제목을 입력하시오"
    game_title = input( game_txt[0] )

    # 값체크    
    # 아무것도 입력하지 않으면 => 아무것도 입력하지 않았습니다. 다시!!\n
    if not game_title: # 부정을 잡는 방법 =  not
        # game_title이 '' 이면, 조건문에 와서는 False로 판단한다
        # ''은 곧 아무거솓 입력하지 않으면이다 
        print( game_txt[1] )        
    # 20자를 초과 입력하면(>)     => 입력하신 "xx" 게임 제목은 최대 20자(현재 %s자 입력)를 초과할수 없습니다. 다시 입력하세요..\n
    elif len(game_title) > 20:
        print( game_txt[2] % (game_title, len(game_title)) )        
    # 정상입력
    else:
        
        # 정상 입력하면 해당 반복문을 빠져나간다
        break
print ( '[%s]'% game_title )

# step 1-2 :
# 게임 프럼프트 출력 (가로 26칸), 한글 제목일 경우 간격 않맞는 부분은 배제
cell_amt = 40
# 포멧팅 사용하는 기호가 서로 다르므로, 다른 케이스로 글자크기를 조절하였다
form = '={0:^%s}=' % (cell_amt-2)
#==============================
print('='*cell_amt)
#=          게임제목           =
print(form.format(game_title))
#=           v1.0.0           =
print(form.format(game_txt[3]))
#==============================
print('='*cell_amt)
# 26이란 수치를 40으로 변경되어도 잘 적응되게 코드를 보정


# step 2 : 
# 게이머의 이름을 입력하세요?
# 입력되지 않으면 => 이름이 입력되지 않았습니다. 다시~'
# flag 변수 => 상화을 통제, 구분하는 변수(변수의 역활)
nameCheck = True
while nameCheck:
    gamer_name = input(game_txt[4])
    if not gamer_name:
        print( game_txt[5] )
        # 다시 조건 체크, 코드를 더이상 진행하지 말고
        continue
    # 이름을 정상 입력했다 => 반복문 그만 끝내라
    nameCheck = False
print( '정상입력', gamer_name  )

game_run = True
while game_run:
    # 게임 변수 초기화 START =====
    # ai값이 없다
    ai_num    = None
    # 시도 횟수
    try_count = 0
    # 게임 변수 초기화 END ======
    while True:
        # step 3 : 
        # 본게임 시작
        # "0 ~ 99사이의 값으로만 AI의 값을 예측하여 입력하세요" 출력하고 다시 입력 대기
        while True:
            gamer_num = input( game_txtEx['GAME_INTRO'] ).strip()
            # '값을 정확하기 입력하세요' 출력하고 다시 입력 대기 -> 아무것도 안넣었다
            # '숫자가 아닙니다' 출력하고 다시 대기 입력
            # '값이 범위를 넘어었습니다. 0~99 사이로 다시 입력' 출력하고, 다시 입력 대기 
            if not gamer_num:
                print(game_txtEx['INPUT_EMPTY'] )
                continue
            elif not gamer_num.isnumeric():# False인 값은 정수값이 될수 없다-> 정수가 아니다
                print(game_txtEx['INPUT_NOT_NUM'] )
                continue
            
            # 문자열의 정수화
            gamer_num = int(gamer_num)
            if gamer_num<0 or gamer_num>99:
                print(game_txtEx['out_of_bound'] )
                continue
            # 범위안에 정수값을 정확하게 획득했다. 반복문 종료
            break

        # step 4 : 
        # AI가 숫자 하나를 랜덤으로 생성한다 0 ~ 99 사이로 1회
        import random
        # ai_num이 값이 없었을때 초기화 해줘라
        if not ai_num:
            ai_num = random.randint(0,99)
            print( 'ai_num=', ai_num)

        try_count +=1
        # step 5 : 판정
        # AI의 숫자보다 유저가 입력한 숫자가 크거나 작으면 코멘트를 해준다 => 맞출때까지 반복
        if gamer_num > ai_num:
            print(game_txtEx['check_err01'])
        elif gamer_num < ai_num:
            print(game_txtEx['check_err02'])
        else: # 정답
            print(game_txtEx['check_success'].format(
                gamer_num,
                ai_num,
                score=(100-try_count*10),
                cnt=try_count,
                name=gamer_name
            ) )
            # 정답이면 
            # 정답입니다. 게이머:{0}, AI:{1}
            #        {name}님의 총 시도 횟수는 {cnt}회 입니다.
            #        획득 점수는 {score}점 입니다.
            # 점수 : 100-시도횟수*10
            break

    # step6 :
    # 다시 게임을 할까요?(yes/no) 대소문자 관계 없이 입력
    # '정확하게 (yes/no)로 입력하세요' 6
    # no => 'game over !! bye bye~'7
    # yes => 본게임 시작 으로 이동하여 진행
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

