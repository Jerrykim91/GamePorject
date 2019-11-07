x = 10
y = 10 # 좌표값
width  = 64
height = 64 # 블록 사이즈 인가??
vel = 5
Screen_Width  = 500  # 창 너비
Screen_Height = 400  # 창 높이
# BLOCK_SIZE    = 10   # 블록 고정
isJump = False
jumpCount = 10
left  = False
right = False
walkCount = 0


# 여러가지 색 // 0-255 ( R, B, G )
RED    = 255, 0, 0       # 적색:   적 255, 녹   0, 청   0
GREEN  = 0, 255, 0       # 녹색:   적   0, 녹 255, 청   0
BLUE   = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127     # 보라색: 적 127, 녹   0, 청 127
BLACK  = 0, 0, 0         # 검은색: 적   0, 녹   0, 청   0
GRAY   = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE  = 255, 255, 255   # 하얀색: 적 255, 녹 255, 청 255