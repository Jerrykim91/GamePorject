# GUI 연습  
import tkinter as tk # 창 생성 

Window = tk.Tk()
# window 창 설정 
Window.title( "제목" )
Window.geometry( "500x500+200+100" ) # ("너비 x 높이 + x좌표 + y좌표")
# 배치 (위젯)
label = tk.Label( Window, text= "입력하세요" )
label.pack()
display = tk.Entry( Window, width=30 )
display.pack()

# Window.resizeable(False, False) # 윈도우 창 크기 조절 여부 조절 -> 상수도 입력가능 ( 상하, 좌우 )

# 함수 
def func(event):
    print(tk.Entry.get(display)) # 입력창에 들어있는 값을 출력 해준다. 
    # print('enter pressed ~') # 임시 // 문자열만 출력 


Window.bind('<Return>',func) # 엔터키 이벤트를 함수에 연결

Window.mainloop()
