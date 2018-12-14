# in distance matrix a to c.
# if path a --> c include point b. Then a --> b + b --> c paths should = a --> c
# so we can remove things where its start -> bunny -> bunker is greater than time limit.  They can never be included.


def answer(times, time_limit):
    size = len(times)
    # Floyd-Warshall algorithm. Taken from Wikipedia tbh
    # Creates distance matrix. Shortest path from a -> b is times[a][b]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]
    # (For test case 3)
    # Checks for negative cycles. If there is. You have infinte time. You can save all the bunnies
    for i in range(size):
        if times[i][i] != 0:
            return range(size-2)
    # 0 = False (not visited), 1 = True (visited)
    visited_bunnies = [0] * (size-2)
    c, v = crawler(0, 0, visited_bunnies, time_limit, times, 0)
    ret = list()
    # Convert from visited to the index of the bunnies for answer
    for idx, x in enumerate(v):
        if x == 1:
            ret.append(idx)
    return ret


def crawler(pos, path_length, visited, time_limit, times, visit_count):
    # Can't save this bunny at pos.
    # Shortest path from here to end is too long.
    if times[pos][len(times)-1] + path_length > time_limit:
        return
    # Base case: Saved all bunnies.
    if 0 not in visited:
        return visit_count, visited
    # Keep track of best track record
    most_visited = visited[:]
    mv_count = visit_count
    # Only go travel to unvisited bunnies
    for idx, visit_status in enumerate(visited):
        visited_copy = visited[:]
        # not yet visited
        if visit_status == 0:
            visited_copy[idx] = 1
            check = crawler(idx+1, path_length + times[pos][idx+1], visited_copy, time_limit, times, visit_count + 1)
            if check is None:
                c = visit_count
                v = visited
            else:
                c, v = check
            if c > mv_count:
                mv_count = c
                most_visited = v
    return mv_count, most_visited
