import numpy as np
from utils import read_file

file_path = './input/day4.txt'


def parse_file(file_content):
    blind_split = file_content.split('\n')
    nums = blind_split.pop(0)
    nums = [int(x) for x in nums.split(',')]

    boards = []
    board = []
    for item in blind_split:
        if item == '' and len(board) > 0:
            boards.append(np.array(board))
            board = []
            continue
            # start new board
        elif item == '' and len(board) == 0:
            continue

        content = [int(x) for x in item.split()]
        board.append(content)
    return nums, boards


def refresh(file_path=file_path):
    nums, boards = parse_file(read_file(file_path))
    return nums, boards


nums, boards = refresh()


def update_board(num, board):
    """update individual board with -1

    Args:
        num (int): element to update
        board (np.array, optional): board to be updated. Defaults to board.

    Returns:
        np.array: updated board
    """
    board[board == num] = -1
    return board


def board_loop(num, boards=boards):
    for i, board in enumerate(boards):
        boards[i] = update_board(num, board)
        if check_winner(boards[i]):
            print("winner winner chicken dinner")
            return boards, i
        else:
            pass
    return boards, None


def check_winner(board):
    row, col = board.shape
    checks = []
    for r in range(row):
        checks.append(np.all(board[r, :] == -1))
    for c in range(col):
        checks.append(np.all(board[:, c] == -1))
    return np.any(checks)


i = 0
flag = None
while flag is None and i < len(nums):
    last_num = nums[i]
    boards, flag = board_loop(last_num)
    i += 1

winner_board = boards[flag]
print('winner board :', winner_board)
print(np.sum(winner_board[winner_board != -1]) * last_num)

#########################################################
# part 2
nums, boards = refresh()


def board_loop_mod(num, boards=boards):
    for i, board in enumerate(boards):

        boards[i] = update_board(num, board)

    for i, board in enumerate(boards):
        if check_winner(boards[i]):
            if len(boards) > 1:
                del boards[i]
            else:
                return boards, i
        else:
            pass

    return boards, None


j = 0
flag = None
while flag is None:
    last_num = nums[j]
    boards, flag = board_loop_mod(last_num)
    j += 1

last_board = boards[0]
print(last_num)
print('part 2: ', np.sum(last_board[last_board != -1]) * last_num)
