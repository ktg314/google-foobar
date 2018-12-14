MAX = 400


# Helper to 'deep' copy 2D arrays.
def copy(a):
    return [row[:] for row in a]


def answer(maze):
    # Init
    empty_solution_maze = [[MAX for x in maze[0]] for y in maze]
    solution_maze = copy(empty_solution_maze)
    default_path = maze_solver(maze, solution_maze)

    if default_path is not None:
        shortest_path = default_path
    else:
        shortest_path = MAX

    # For each wall, convert 1 to 0 and run maze_solver to see if we get a new shorter path
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 1:
                new_maze = copy(maze)
                new_maze[i][j] = 0
                new_solution_maze = copy(empty_solution_maze)
                new_maze_path = maze_solver(new_maze, new_solution_maze)
                if new_maze_path is not None:
                    if new_maze_path < shortest_path:
                        shortest_path = new_maze_path
    return shortest_path


# Takes maze and solution_maze and fills solution_maze with shortest path to each pathable square
# Returns : path length to bottom right corner
def maze_solver(maze, solution_maze):
    crawler((0, 0), maze, solution_maze, 1)
    height = len(maze[0])
    width = len(maze)
    return solution_maze[width - 1][height - 1]


# Recursively visits every coordinate, fills with shortest path number to get there in solution_maze
def crawler(coordinate, maze, solution_maze, path_length):
    # Init
    height = len(maze[0])
    width = len(maze)
    x = coordinate[0]
    y = coordinate[1]
    # Found a shorter path. Default is 400 if unreached
    if solution_maze[x][y] > path_length:
        solution_maze[x][y] = path_length
    else:
        return

    paths = list()
    # Edge cases for cardinal movement
    if x != 0:
        paths.append((x - 1, y))
    if x != width - 1:
        paths.append((x + 1, y))
    if y != 0:
        paths.append((x, y - 1))
    if y != height - 1:
        paths.append((x, y + 1))
    # For every path which isn't a wall, crawl
    for path in paths:
        if maze[path[0]][path[1]] == 0:
            crawler(path, maze, solution_maze, path_length + 1)
    return
