import numpy as np

from state import State, UltimateTTT_Move

def blocksO(blocks):
    index = 0
    for i in range(0, 9):
        count = 0
        if i != 4:
            for row in blocks[i]:
                for cell in row:
                    if cell == -1:
                        count += 1
            if count > index:
                index = i
    return index

def count_X(blocks):
    count = 0
    for i in [z for y in blocks for x in y for z in x]:
        if i == 1:
            count += 1
    return count

def count_O(blocks):
    count = 0
    for i in [z for y in blocks for x in y for z in x]:
        if i == -1:
            count += 1
    return count

def select_move(cur_state, remain_time):
    valid_moves = cur_state.get_valid_moves
    blocks = cur_state.blocks

    if count_X(blocks) == 0 and count_O(blocks) == 0:
        return UltimateTTT_Move(4, 1, 1, 1)

    if count_X(blocks) < 8:
        for valid_move in valid_moves:
            if valid_move.x == 1 and valid_move.y == 1:
                return valid_move

    if count_X(blocks) == 8:
        previous_move = cur_state.previous_move
        x = previous_move.x
        y = previous_move.y
        return UltimateTTT_Move(x*3 + y, x, y, 1)

    if count_X(blocks) > 8 and count_X(blocks) < 20:
        index_local_board = blocksO(blocks)
        x = index_local_board // 3
        y = index_local_board % 3


        if len(valid_moves) > 9:
            for valid_move in valid_moves:
                if valid_move.x == x and valid_move.y == y and valid_move.index_local_board == 8 - index_local_board:
                    return valid_move
            for valid_move in valid_moves:
                if valid_move.x == 2 - x and valid_move.y == 2 - y and valid_move.index_local_board == 8 - index_local_board:
                    return valid_move
            
            
        for valid_move in valid_moves:
            if valid_move.x == x and valid_move.y == y:
                return valid_move

    for valid_move in valid_moves:
        new_state = State(cur_state)
        count = new_state.count_X
        try:
            new_state.act_move(valid_move)
        except:
            continue
        if new_state.count_X > count:
            return valid_move

    best_move = np.random.choice(valid_moves)

    return best_move
