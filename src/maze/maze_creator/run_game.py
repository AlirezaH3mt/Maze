from main_matrix import matrixStructure
from maze_printer import mazePrinter
from maze_creator import mazeBacktracking, goalPositionAdder
from player import addPlayer, movePlayer, player_win
import subprocess
import os


def clear_console():
    command = "cls" if os.name == "nt" else "clear"

    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"error : {e}")


MATRIX_SIZE = 21
STARTING_POS = (1, 1)
WALL_CHAR = "#"
PLAYER_CHAR = "P"
GOAL_CHAR = "G"
player_pos = STARTING_POS
goal_pos = ()

maze = matrixStructure(
    matrix_size=MATRIX_SIZE, starting_pos=STARTING_POS, wall_char=WALL_CHAR
)

mazeBacktracking(maze, starting_pos=STARTING_POS, wall_char=WALL_CHAR)
goal_pos = goalPositionAdder(maze, MATRIX_SIZE, GOAL_CHAR)
addPlayer(maze, player_pos, PLAYER_CHAR)

game_running = True
while game_running:
    clear_console()
    mazePrinter(maze)

    player_input = input("(w, d, s, a, q(Quit)) => ").lower()

    if player_input == "q":
        game_running = False

    player_pos = movePlayer(maze, player_pos, PLAYER_CHAR, GOAL_CHAR, player_input)

    hasWon = player_win(player_pos, goal_pos)
    if hasWon:
        game_running = False
        print("Congradulations, you won!")
