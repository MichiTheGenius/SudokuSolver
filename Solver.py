

board = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,2,0],
[0,0,0,0,0,0,0,0,0]
]

def print_board():
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-----------")
        for column in range(9):
            if column % 3 == 0 and column != 0:
                print("|",end="")
            print(board[row][column], end="")
        print()

print_board()
