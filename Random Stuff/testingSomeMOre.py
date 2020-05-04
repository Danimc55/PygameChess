WINDOWWIDTH = 800
WINDOWHEIGHT = 800

BOARDWIDTH = 8
BOARDHEIGHT = 8

BOXWIDTH = WINDOWWIDTH / BOARDWIDTH
BOXHEIGHT = WINDOWHEIGHT / BOARDHEIGHT

board = []
for x in range(0, BOARDWIDTH):
    line = []
    for y in range(0, BOARDHEIGHT):
        if (x + y) % 2 == 0:
            line.append((0, 0, 0))
        else:
            line.append((255, 255, 255))
    board.append(line)

for x, line in enumerate(board):
    for y, box in enumerate(line):
        print(x * BOXWIDTH, y * BOXHEIGHT, BOXWIDTH, BOXHEIGHT)