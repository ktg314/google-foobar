def answer(str_n):
    n = long(str_n)
    return str(beatty_sum(n))


# First 100 digits of sqrt(2) - 1 as a long type
root2m1 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727


# Summation of a beatty sequence
# https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
def beatty_sum(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    np = root2m1*n//(10**100)
    val = n*np + n*(n+1)/2 - np*(np+1)/2
    if np == 0:
        return val
    return val - beatty_sum(np)
