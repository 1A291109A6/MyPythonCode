import random

#0:empty,1:〇,2:×

# 0| 1| 2
#--------
# 3| 4| 5
#--------
# 6| 7| 8


def draw_board():
    for i in range(0,3):
        row = ""
        for j in range(0,3):
            if board[3 * i + j] == 0:
                row += "　"
            elif board[3 * i + j] == 1:
                row += "〇"
            else:
                row += "×"
            if not j == 2:
                row += "|"
        print(row)
        if not i == 2:
            print("-" * 8)

def put_OX(OXtype,position,board):
    new_board = []
    for i in range(0,9):
        if i == position:
            new_board.append(OXtype)
        else:
            new_board.append(board[i])
    return new_board

def reach_checker(OXtype,board):
    #vertical
    reach_list = []
    for i in range(0,3):
        count = 0
        for j in range(0,3):
            if board[3 * j + i] == OXtype:
                count += 1
        if count == 2:
            reach_list.append(i + 1)
    #horizontal
    for i in range(0,3):
        count = 0
        for j in range(0,3):
            if board[3 * i + j] == OXtype:
                count += 1
        if count == 2:
            reach_list.append(i + 4)
    #diagonal(top left)
    count = 0
    for i in range(0,3):
        if board[4 * i] == OXtype:
            count += 1
    if count == 2:
        reach_list.append(7)
    #diagonal(top right)
    count = 0
    for i in range(0,3):
        if board[2 * i + 2] == OXtype:
            count += 1
    if count == 2:
        reach_list.append(8)
    return reach_list

def judgment(OXtype,board):
    #vertical
    reach_list = []
    for i in range(0,3):
        count = 0
        for j in range(0,3):
            if board[3 * j + i] == OXtype:
                count += 1
        if count == 3:
            return True
    #horizontal
    for i in range(0,3):
        count = 0
        for j in range(0,3):
            if board[3 * i + j] == OXtype:
                count += 1
        if count == 3:
            return True
    #diagonal(top left)
    count = 0
    for i in range(0,3):
        if board[4 * i] == OXtype:
            count += 1
    if count == 3:
        return True
    #diagonal(top right)
    count = 0
    for i in range(0,3):
        if board[2 * i + 2] == OXtype:
            count += 1
    if count == 3:
        return True
    return False

def search_empty(board):
    empty_list = []
    for i in range(0,9):
        if board[i] == 0:
            empty_list.append(i)
    return empty_list

#main

board = [0,0,0,0,0,0,0,0,0]
draw_board()
select = int(input("your turn >>"))
board = put_OX(1,select,board)
draw_board()
print()
if select == 0:
    candidate = [1,3,4]
if select == 1:
    candidate = [0,2,3,4,5]
if select == 2:
    candidate = [1,4,5]
if select == 3:
    candidate = [0,1,4,6,7]
if select == 4:
    candidate = [0,2,6,8]
if select == 5:
    candidate = [1,2,4,7,8]
if select == 6:
    candidate = [3,4,7]
if select == 7:
    candidate = [3,4,5,6,8]
if select == 8:
    candidate = [4,5,7]

board = put_OX(2,candidate[random.randint(0,len(candidate) - 1)],board)
draw_board()
print()

while True:
    select = int(input("your turn >>"))
    board = put_OX(1,select,board)
    draw_board()
    if judgment(1,board) == True:
        print("WIN!!")
        break
    if search_empty(board) == []:
        print("DRAW")
        break
    print()
    empty_list = search_empty(board)
    board = put_OX(2,empty_list[random.randint(0,len(empty_list) - 1)],board)
    draw_board()
    if judgment(2,board) == True:
        print("LOSE...")
        break
