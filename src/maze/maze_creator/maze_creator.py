from main_matrix import matrix_structure
from maze_printer import maze_printer


def check_possible_directions(maze, current_pos, wall_char):
    directions = ["Up", "Right", "Down", "Left"]
    available_directions = []

    if (
        current_pos[0] - 2 >= 0
        and maze[current_pos[0] - 2][current_pos[1]] == wall_char
    ):
        available_directions.append(directions[0])
    if (
        current_pos[1] + 2 < len(maze)
        and maze[current_pos[0]][current_pos[1] + 2] == wall_char
    ):
        available_directions.append(directions[1])
    if (
        current_pos[0] + 2 < len(maze)
        and maze[current_pos[0] + 2][current_pos[1]] == wall_char
    ):
        available_directions.append(directions[2])
    if (
        current_pos[1] - 2 >= 0
        and maze[current_pos[0]][current_pos[1] - 2] == wall_char
    ):
        available_directions.append(directions[3])

    return available_directions


def maze_backtracking(maze):
    pass


MATRIX_SIZE = 5
STARTING_POS = (MATRIX_SIZE // 2, MATRIX_SIZE // 2)
WALL_CHAR = "#"
PLAYER_CHAR = "@"

maze = matrix_structure(
    matrix_size=MATRIX_SIZE, starting_pos=STARTING_POS, wall_char=WALL_CHAR
)
maze_printer(maze)
