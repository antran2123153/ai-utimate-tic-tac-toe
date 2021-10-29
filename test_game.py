import pygame, sys
from pygame.locals import K_TAB, QUIT, K_RIGHT
from state import State, State_2
import time
from importlib import import_module


color = {
    "black": pygame.Color(0, 0, 0),
    "white": pygame.Color(255, 255, 255),
    "blue": pygame.Color(50, 255, 255),
    "orange": pygame.Color(255, 120, 0),
}
small_image = {
    1: pygame.image.load("images/small_x.png"),
    -1: pygame.image.load("images/small_o.png"),
}
large_image = {
    1: pygame.image.load("images/large_x.png"),
    -1: pygame.image.load("images/large_o.png"),
}

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")


def draw(state: State_2):
    screen.fill("white")

    for x in range(3):
        for y in range(3):
            pygame.draw.rect(screen, color["white"], (x * 200, y * 200, 200, 200))

    if state.previous_move != None:
        next_block = state.previous_move.x * 3 + state.previous_move.y
        pygame.draw.rect(
            screen,
            color["blue"],
            ((next_block % 3) * 200, (next_block // 3) * 200, 200, 200),
        )

        i = state.previous_move.index_local_board
        pygame.draw.rect(
            screen,
            color["orange"],
            (
                (i % 3) * 200 + state.previous_move.y * 50 + 25,
                (i // 3) * 200 + state.previous_move.x * 50 + 25,
                50,
                50,
            ),
        )

    for k in range(9):
        value = state.global_cells[k]
        if value != 0:
            picture = large_image[value]
            picture = pygame.transform.scale(picture, (100, 100))
            screen.blit(picture, ((k % 3) * 200 + 50, (k // 3) * 200 + 50))

    for x in range(3):
        for y in range(3):
            for i in [1, 2]:
                pygame.draw.line(
                    screen,
                    color["black"],
                    (x * 200 + i * 50 + 25, y * 200 + 25),
                    (x * 200 + i * 50 + 25, y * 200 + 175),
                    2,
                )
                pygame.draw.line(
                    screen,
                    color["black"],
                    (x * 200 + 25, y * 200 + i * 50 + 25),
                    (x * 200 + 175, y * 200 + i * 50 + 25),
                    2,
                )

    for i in range(9):
        local_board = state.blocks[i]
        for x in range(3):
            for y in range(3):
                value = local_board[x, y]
                if value != 0:
                    screen.blit(
                        small_image[value],
                        ((i % 3) * 200 + y * 50 + 35, (i // 3) * 200 + x * 50 + 35),
                    )

    for i in [1, 2]:
        pygame.draw.line(screen, color["black"], (i * 200, 0), (i * 200, 600), 3)
        pygame.draw.line(screen, color["black"], (0, i * 200), (600, i * 200), 3)

    pygame.display.update()


def play_step_by_step(player_X, player_O, rule=1):
    player_1 = import_module(player_X)
    player_2 = import_module(player_O)
    if rule == 1:
        state = State()
    else:
        state = State_2()
    turn = 0
    remain_time_X = 120
    remain_time_O = 120
    is_game_done = False

    while True:
        draw(state)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if state.game_over or is_game_done:
                continue

            if event.type == pygame.KEYDOWN:
                if event.key == K_TAB or event.key == K_RIGHT:

                    start_t = time.time()
                    if state.player_to_move == 1:
                        new_move = player_1.select_move(state, remain_time_X)
                        elapsed_time = time.time() - start_t
                        remain_time_X -= elapsed_time
                    else:
                        new_move = player_2.select_move(state, remain_time_O)
                        elapsed_time = time.time() - start_t
                        remain_time_O -= elapsed_time

                    if elapsed_time > 10 or not new_move:
                        is_game_done = True

                    if (remain_time_O < -0.1) or (remain_time_X < -0.1):
                        is_game_done = True

                    state.act_move(new_move)
                    turn += 1
                    if turn == 81:
                        is_game_done = True


def play_auto(player_X, player_O, rule=1):
    player_1 = import_module(player_X)
    player_2 = import_module(player_O)
    if rule == 1:
        state = State()
    else:
        state = State_2()
    turn = 0
    remain_time_X = 120
    remain_time_O = 120
    is_game_done = False

    while True:
        draw(state)
        # delay drawing
        # time.sleep(2)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if state.game_over or is_game_done:
            continue

        start_t = time.time()
        if state.player_to_move == 1:
            new_move = player_1.select_move(state, remain_time_X)
            elapsed_time = time.time() - start_t
            remain_time_X -= elapsed_time
        else:
            new_move = player_2.select_move(state, remain_time_O)
            elapsed_time = time.time() - start_t
            remain_time_O -= elapsed_time

        if (
            elapsed_time > 10
            or not new_move
            or (remain_time_O < -0.1)
            or (remain_time_X < -0.1)
        ):
            is_game_done = True
            continue

        state.act_move(new_move)
        turn += 1


# play_auto("minimax", "random_agent")
play_auto("random_agent", "minimax")

# play_step_by_step('random_agent', '3')
