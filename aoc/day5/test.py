# note: using // for every division because / will return float, while // returns floor(num)
def determine_start(map):
    """
    determine the starting point for this map
    @param map: garden as a 2D matrix
    @return: the tuple (y, x) representing the starting location
    """
    n, m = len(map[0]), len(map)
    if n % 2 == 1 and m % 2 == 1:  # both odd, pick center
        return (n - 1) / 2, (m - 1) / 2
    elif n % 2 == 1:  # n odd, m even, so check both m
        center_n = (n - 1) // 2
        if map[center_n][(m // 2)] > map[center_n][(m - 1) // 2]:
            return center_n, m // 2
        else:
            return center_n, (m - 1) // 2
    elif m % 2 == 1:  # m odd, check both n
        center_m = (m - 1) // 2
        if map[n // 2][center_m] > map[(n - 1) // 2][center_m]:
            return center_m, n // 2
        else:
            return center_m, (n - 1) // 2
    else:  # both even, check all 4 center squares
        lower_n = (n - 1) // 2
        upper_n = n // 2
        lower_m = (m - 1) // 2
        upper_m = m // 2
        max_carrots = max(map[lower_n][lower_m], map[lower_n][upper_m], map[upper_n][lower_m], map[upper_n][upper_m])
        if map[lower_n][lower_m] == max_carrots:
            return lower_n, lower_m
        elif map[lower_n][upper_m] == max_carrots:
            return lower_n, upper_m
        elif map[upper_n][lower_m] == max_carrots:
            return upper_n, lower_m
        else:
            return upper_n, upper_m


def determine_max_eaten(map):
    """
    performs greedy traversal of the map
    @param map: garden as a 2D matrix
    @return: maximum number of carrots eaten
    """
    n, m = len(map[0]), len(map)
    curr_y, curr_x = determine_start(map)
    eaten = 0  # eat starting point
    has_moves = True
    while has_moves:
        eaten += map[curr_x][curr_y]
        map[curr_x][curr_y] = 0  # eaten this, set to 0

        up = map[curr_x - 1][curr_y] if curr_x > 0 else 0
        down = map[curr_x + 1][curr_y] if curr_x < m - 1 else 0
        right = map[curr_x][curr_y + 1] if curr_y < n - 1 else 0
        left = map[curr_x][curr_y - 1] if curr_y > 0 else 0

        if (up, down, right, left) == (0, 0, 0, 0):  # bed time
            has_moves = False
        else:
            best_move = max(up, down, right, left)
            if best_move == up:
                curr_x -= 1
            elif best_move == down:
                curr_x += 1
            elif best_move == right:
                curr_y += 1
            elif best_move == left:
                curr_y -= 1

    return eaten


garden = [[5, 7, 8, 6, 3],
          [0, 0, 7, 0, 4],
          [4, 6, 3, 4, 9],
          [3, 1, 0, 5, 8]]

print(determine_max_eaten(garden))
