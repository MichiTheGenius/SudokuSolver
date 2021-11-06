
board = [
[1,0,0,0,0,0,0,0,0],
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

def is_number_in_row(number,row):
    for column in range(9):
        if board[row][column] == number:
            return True
    return False

def is_number_in_column(number,column):
    for row in range(9):
        if board[row][column] == number:
            return True
    return False

def is_number_in_box(number,row,column):
    box_row = row - row % 3
    box_column = column - column % 3
    for i in range(box_row,box_row+3):
        for j in range(box_column,box_column+3):
            if board[i][j] == number:
                return True
    return False

def is_valid_place(number,row,column):
    return not is_number_in_row(number,row) and not is_number_in_column(number,column) and not is_number_in_box(number,row,column)



print_board()
