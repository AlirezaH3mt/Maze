import random as rnd


def checkPossibleDirections(maze, current_pos, wall_char):
    directions = ["Up", "Right", "Down", "Left"]
    available_directions = {}

    if (
        current_pos[0] - 2 >= 0
        and maze[current_pos[0] - 2][current_pos[1]] == wall_char
    ):
        available_directions[directions[0]] = (current_pos[0] - 2, current_pos[1])
    if (
        current_pos[1] + 2 < len(maze)
        and maze[current_pos[0]][current_pos[1] + 2] == wall_char
    ):
        available_directions[directions[1]] = (current_pos[0], current_pos[1] + 2)
    if (
        current_pos[0] + 2 < len(maze)
        and maze[current_pos[0] + 2][current_pos[1]] == wall_char
    ):
        available_directions[directions[2]] = (current_pos[0] + 2, current_pos[1])
    if (
        current_pos[1] - 2 >= 0
        and maze[current_pos[0]][current_pos[1] - 2] == wall_char
    ):
        available_directions[directions[3]] = (current_pos[0], current_pos[1] - 2)

    return available_directions


def midWallBreaker(maze, random_dir, dir_coord):
    if random_dir == "Up":
        maze[dir_coord[0] + 1][dir_coord[1]] = " "
    elif random_dir == "Right":
        maze[dir_coord[0]][dir_coord[1] - 1] = " "
    elif random_dir == "Down":
        maze[dir_coord[0] - 1][dir_coord[1]] = " "
    else:
        maze[dir_coord[0]][dir_coord[1] + 1] = " "


def mazeBacktracking(maze, starting_pos, wall_char):
    digger_pos = starting_pos
    taken_steps_list = [starting_pos]

    while len(taken_steps_list) > 0:
        possible_dirs = checkPossibleDirections(
            maze=maze, current_pos=digger_pos, wall_char=wall_char
        )

        if len(possible_dirs) != 0:
            random_dir = rnd.choice(list(possible_dirs.keys()))
            dir_coord = possible_dirs[random_dir]
            # print(f"random_dir: {random_dir}, coord : {dir_coord}")
            maze[dir_coord[0]][dir_coord[1]] = " "
            midWallBreaker(maze, random_dir, dir_coord)
            taken_steps_list.append(dir_coord)
            digger_pos = dir_coord

        else:
            digger_pos = taken_steps_list[-1]
            taken_steps_list.pop()


def goalPositionAdder(maze, matrix_size, goal_char):
    isGoalSet = False
    while not isGoalSet:
        random_goal_pos = rnd.randint(1, matrix_size - 2)
        if maze[random_goal_pos][matrix_size - 2] == " ":
            maze[random_goal_pos][matrix_size - 2] = goal_char
            isGoalSet = True
