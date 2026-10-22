def addPlayer(maze, starting_pos, player_char):
    maze[starting_pos[0]][starting_pos[1]] = player_char


def checkPossibleDirections(maze, player_pos):
    possible_coords = {}
    if maze[player_pos[0] - 1][player_pos[1]] == " ":
        possible_coords["Up"] = (player_pos[0] - 1, player_pos[1])
    if maze[player_pos[0]][player_pos[1] + 1] == " ":
        possible_coords["Right"] = (player_pos[0], player_pos[1] + 1)
    if maze[player_pos[0] + 1][player_pos[1]] == " ":
        possible_coords["Down"] = (player_pos[0] + 1, player_pos[1])
    if maze[player_pos[0]][player_pos[1] - 1] == " ":
        possible_coords["Left"] = (player_pos[0], player_pos[1] - 1)
    return possible_coords


def movePlayer(maze, player_pos, player_char, player_input):
    possible_dirs = checkPossibleDirections(maze, player_pos)

    if player_input == "w" and "Up" in possible_dirs.keys():
        up = possible_dirs["Up"]
        maze[up[0]][up[1]] = player_char
        maze[player_pos[0]][player_pos[1]] = " "
        player_pos = up
    elif player_input == "d" and "Right" in possible_dirs.keys():
        right = possible_dirs["Right"]
        maze[right[0]][right[1]] = player_char
        maze[player_pos[0]][player_pos[1]] = " "
        player_pos = right
    elif player_input == "s" and "Down" in possible_dirs.keys():
        down = possible_dirs["Down"]
        maze[down[0]][down[1]] = player_char
        maze[player_pos[0]][player_pos[1]] = " "
        player_pos = down
    elif player_input == "a" and "Left" in possible_dirs.keys():
        left = possible_dirs["Left"]
        maze[left[0]][left[1]] = player_char
        maze[player_pos[0]][player_pos[1]] = " "
        player_pos = left

    return player_pos
