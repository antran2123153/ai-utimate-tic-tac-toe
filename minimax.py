import numpy as np
from state import State
import time

MAX_DEPTH = 5

MAX = 1000
MIN = -1000

SCORE_1 = 1
SCORE_2 = 2
SCORE_3 = 3

SCORE_4 = 6
SCORE_5 = 8
SCORE_6 = 10

SCORE_WIN_BLOCK = 50
SCORE_WIN_GAME = 500

def isWinGame(block, player):
    indexs = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for i in indexs:
        if block[i[0]] == block[i[1]] == block[i[2]] == player:
            return True
    return False

def scoreBlock(block, player):
    score = 0
    if block[0][0] == player:
        score += SCORE_1
    if block[0][2] == player:
        score += SCORE_1
    if block[2][0] == player:
        score += SCORE_1
    if block[2][2] == player:
        score += SCORE_1
    if block[1][1] == player:
        score += SCORE_2

    for i in range(0, 3):
        if block[i][0] == block[i][1] == player or block[i][1] == block[i][2] == player:
            score += SCORE_3
        if block[0][i] == block[1][i] == player or block[1][i] == block[2][i] == player:
            score += SCORE_3

    if block[0][0] == block[1][1] or block[1][1] == block[2][2]:
        score += SCORE_3
    if block[0][2] == block[1][1] or block[1][1] == block[2][0]:
        score += SCORE_3

    return score
        

def heuritic(cur_state, cur_player, player):
    blocks = cur_state.blocks
    global_cells = cur_state.global_cells
    
    if isWinGame(global_cells, cur_player):
        if cur_player == player:
            return SCORE_WIN_GAME
        return -SCORE_WIN_GAME
    
    score = 0

    for i in range(0, 9):
        if global_cells[i] == cur_player:
            score += SCORE_WIN_BLOCK
        elif global_cells[i] == 0:
            score += scoreBlock(blocks[i], cur_player)
    
    score += len([x for x in global_cells if x == cur_player])*SCORE_4
    for i in [0, 2, 6, 8]:
        if global_cells[i] == cur_player:
            score += SCORE_5
    if global_cells[4] == cur_player:
        score += SCORE_6
    
    if cur_player == player:
        return score
    return -score


def minimax(depth, cur_state, cur_player, player, alpha, beta):
    valid_moves = cur_state.get_valid_moves
    if len(valid_moves) == 0 or depth == MAX_DEPTH:
        return heuritic(cur_state, cur_player, player) + heuritic(cur_state, -cur_player, player)

    if cur_player == player:
        best = MIN
        for valid_move in valid_moves:
            new_state = State(cur_state)
            try:
                new_state.act_move(valid_move)
            except:
                continue
            val = minimax(depth + 1, new_state, -cur_player, player, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha: 
                break
    else:
        best = MAX
        for valid_move in valid_moves:
            new_state = State(cur_state)
            try:
                new_state.act_move(valid_move)
            except:
                continue
            val = minimax(depth + 1, new_state, -cur_player, player, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
    return best
	

def select_move(cur_state, remain_time):
    valid_moves = cur_state.get_valid_moves
    n = len(valid_moves)
    # print(valid_moves)
    
    if n == 0:
        return None

    best_value = MIN
    best_move = np.random.choice(valid_moves)
    player = cur_state.player_to_move

    for valid_move in valid_moves:
        new_state = State(cur_state)
        try:
            new_state.act_move(valid_move)
        except:
            continue
        if n > 11:
            value = minimax(3, new_state, -player, player, MIN, MAX)
        elif n > 9 and n <= 11:
            value = minimax(2, new_state, -player, player, MIN, MAX)
        elif n > 5 and n <= 9:
            value = minimax(1, new_state, -player, player, MIN, MAX)
        elif n > 3 and n <= 5:
            value = minimax(0, new_state, -player, player, MIN, MAX)
        else:
            value = minimax(1, new_state, -player, player, MIN, MAX)    
        if value > best_value:
            best_value = value
            best_move = valid_move
    return best_move
