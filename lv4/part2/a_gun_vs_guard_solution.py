from math import ceil
from fractions import gcd


def answer(dimensions, your_position, guard_position, distance):
    # Used **2 instead of sqrt to avoid rounding errors
    MAX_DIST = distance ** 2
    initial_x_distance = guard_position[0] - your_position[0]
    initial_y_distance = guard_position[1] - your_position[1]
    # Simple base cases
    if initial_x_distance ** 2 + initial_y_distance ** 2 > MAX_DIST:
        return 0
    elif initial_x_distance ** 2 + initial_y_distance ** 2 == MAX_DIST:
        return 1

    # West/Left & South/Down
    x_west_start = -1 * (your_position[0] + guard_position[0])
    y_south_start = -1 * (your_position[1] + guard_position[1])

    # East/Right & North/Up
    x_east_start = 2 * dimensions[0] - guard_position[0] - your_position[0]
    y_north_start = 2 * dimensions[1] - guard_position[1] - your_position[1]

    # Max we have to check due to dist / height or width ratio
    x_max_reflects = int(ceil(distance / dimensions[0])) + 2
    y_max_reflects = int(ceil(distance / dimensions[1])) + 2

    # Double while loop that adds all shots that are within MAX_DIST
    # Only rule being don't flip on same border twice in a row.
    # Doesn't matter if the actual path works or not with the order of
    # North / East, etc. flips as N/S and E/W flips don't interfere with
    # one another.
    shots = list()
    i = 0
    x_arr = [initial_x_distance, initial_x_distance]
    while i < x_max_reflects:
        j = 0
        # First flip is different
        if i == 1:
            x_arr = [x_east_start, x_west_start]
        # Initial shots without hitting N or S wall.
        for x in x_arr:
            if x ** 2 + initial_y_distance ** 2 <= MAX_DIST:
                shots.append([x, initial_y_distance])

        # Initialize North/South first flips
        y_arr = [y_north_start, y_south_start]
        # Flipping up/down until too big
        while j < y_max_reflects:
            add_list = [(x, y) for x in x_arr for y in y_arr if x ** 2 + y ** 2 <= MAX_DIST]
            for x, y in add_list:
                shots.append([x, y])
            # Do North/South transformation of point.
            y_arr[0] = -1 * (y_arr[0] + 2 * your_position[1])
            y_arr[1] = -1 * y_arr[1] + 2 * (dimensions[1] - your_position[1])
            # Switch as you can't go NN or SS
            y_arr[0], y_arr[1] = y_arr[1], y_arr[0]
            j += 1

        # Do East/West transformation of point.
        x_arr[0] = -1 * (x_arr[0] + 2 * your_position[0])
        x_arr[1] = -1 * x_arr[1] + 2 * (dimensions[0] - your_position[0])
        # Switch as you can't go EE or WW
        x_arr[0], x_arr[1] = x_arr[1], x_arr[0]
        i += 1

    # Fill shot dictionary with each shot with min length
    # (shots stop once they hit the guard, can't continue)
    shot_dict = dict_with_shortest_path(shots)

    # fill suicide / self shot list
    suicide_x = [i * 2 * dimensions[0] for i in xrange(-1 * x_max_reflects + 1, x_max_reflects)]
    const1 = 2 * (dimensions[0] - your_position[0])
    suicide_x += [i + const1 for i in suicide_x]
    # repeat for y. dim0 -> dim1
    suicide_y = [i * 2 * dimensions[1] for i in xrange(-1 * y_max_reflects + 1, y_max_reflects)]
    const2 = 2 * (dimensions[1] - your_position[1])
    suicide_y += [i + const2 for i in suicide_y]
    temp_suicide = set([(x, y) for x in suicide_x for y in suicide_y])

    # Fill suicide dictionary with shortest dist
    # (again, stops if you hit self)
    suicide = dict_with_shortest_path(temp_suicide)

    # Fills ret list with shots that don't hit yourself
    ret = list()
    for a in shot_dict:
        if a in suicide:
            if suicide.get(a) < shot_dict.get(a):
                # Has to be in suicide and be shorter to not add
                continue
        ret.append(a)

    # You just want the number of shots
    return len(ret)


# Takes list of tuples and returns dictionary with tuples
# mapped to their shortest distance
def dict_with_shortest_path(vec):
    # Return dictionary
    ret_dict = dict()
    for x, y in vec:
        gcf = abs(gcd(x, y))
        diag_dist = x ** 2 + y ** 2
        if gcf != 0:
            x = int(x / gcf)
            y = int(y / gcf)
        # Want no duplicates, only shortest dist
        if (x, y) in ret_dict:
            if ret_dict.get((x, y)) < diag_dist:
                continue
        ret_dict.update({(x, y): diag_dist})
    return ret_dict
