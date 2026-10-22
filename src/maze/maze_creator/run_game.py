from main_matrix import matrixStructure
from maze_printer import mazePrinter
from maze_creator import mazeBacktracking
from maze_creator import goalPositionAdder
from player import addPlayer
from player import checkPossibleDirections
from player import movePlayer

MATRIX_SIZE = 21
STARTING_POS = (1, 1)
WALL_CHAR = "#"
PLAYER_CHAR = "P"
GOAL_CHAR = "G"
player_pos = STARTING_POS

maze = matrixStructure(
    matrix_size=MATRIX_SIZE, starting_pos=STARTING_POS, wall_char=WALL_CHAR
)

mazeBacktracking(maze, starting_pos=STARTING_POS, wall_char=WALL_CHAR)
goalPositionAdder(maze, MATRIX_SIZE, GOAL_CHAR)
addPlayer(maze, player_pos, PLAYER_CHAR)

game_running = True
while game_running:
    mazePrinter(maze)
    player_input = input("(w, d, s, a, q(Quit)) => ")[0].lower()

    if player_input == "q":
        game_running = False

    player_pos = movePlayer(maze, player_pos, PLAYER_CHAR, player_input)
