def maze_printer(maze):
    # Check if maze is valid
    if len(maze) == 0:
        raise ValueError("This matrix does not have proper shape!")
    else:
        for r in maze:
            if len(maze) != len(r):
                raise ValueError("This matrix should be cubic!")

    # Print maze
    for i in range(len(maze)):
        for j in range(len(maze)):
            print(maze[i][j], end=" ")
        print()
