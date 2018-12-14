import math
MAX_BRICKS = 201
memory = [[0 for x in range(MAX_BRICKS)] for y in range(MAX_BRICKS)]


def answer(n):
    return helper(n, n)


def helper(upper_bound, blocks):
    # This returns if the value has been calculated already.
    if memory[upper_bound][blocks] != 0:
        return memory[upper_bound][blocks]
    # Base cases
    if blocks == 1:
        return 1
    if blocks == 2:
        if upper_bound > 2:
            return 1
        else:
            return 0
    # Initialize variables
    combos = 0
    step_height = upper_bound - 1
    remainder = 1
    # +1 for the case where you don't break down the step any further
    if upper_bound > blocks:
        return helper(blocks, blocks) + 1
    if upper_bound < blocks:
        # Check if there are too many blocks to fit under upper_bound step
        if upper_bound*(upper_bound-1)/2 < blocks:
            return 0
        else:
            combos = helper(step_height, blocks - step_height)
            remainder = blocks - upper_bound + 2
            step_height -= 1
    # Not perfect but close enough. Reduce amount of loops.
    lowest_step_possible = math.floor(math.sqrt(2*blocks)) - 1
    while step_height > lowest_step_possible:
        # Again, check if too many blocks to fit under step_height
        if step_height < remainder:
            if (step_height*(step_height-1)/2) < remainder:
                break;
        combos += helper(step_height, remainder)
        step_height -= 1
        remainder += 1
    memory[upper_bound][blocks] = combos
    return combos
