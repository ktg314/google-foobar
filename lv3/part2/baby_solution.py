import math
IMPOSSIBLE = -42


def answer(M, F):
    try:
        mach = int(M)
        facula = int(F)
    except ValueError:
        return "impossible"
    ret = helper(mach, facula)
    if ret == IMPOSSIBLE:
        return "impossible"
    else:
        return str(ret)


# Inputs are ints
def helper(mach, facula):
    # Covers (1, n) and (m, 1) and (1,1) = 0
    if mach == 1:
        return facula - 1
    if facula == 1:
        return mach - 1
    # Fail Case 1
    if mach == facula:
        return IMPOSSIBLE
    if mach > facula:
        big = mach
        small = facula
    else:
        big = facula
        small = mach

    if big % small == 0:
        return IMPOSSIBLE
    generation = int(math.floor(big / small))
    big -= generation * small
    big = int(big)
    help = helper(big, small)
    if help == IMPOSSIBLE:
        return help
    else:
        return generation + help
