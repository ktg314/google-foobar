import math

root5 = math.sqrt(5)
alpha = (1 + root5) / 2
beta = (1 - root5) / 2


def fib(n):
    return math.floor((alpha ** n - beta ** n) / root5)


def answer(total_lambs):
    # RULES
    # 1) most junior = 1 LAMB. At least 1 per team
    # 2) person right above can't have > 2x (Square)
    # 3) s[n] > s[n-1] + s[n-2] (Fib)
    # 4) always check for more henchmen. No limit on ppl. Only max seniority

    # return: max number of hench men vs least
    if total_lambs in [1,2,3]:
        return 0
    # 2**n
    # 1, 2, 4, 8, 16
    # 1, 3, 7, 15
    # x = number of ppl minimum
    x = math.floor(math.log(total_lambs + 1, 2))
    # input 13:
    # log2(13) = 3 // log2(7+1) = 3
    paid = (2 ** x) - 1
    highest_paid = 2 ** (x-1)
    remainder = total_lambs - paid
    # checking for rule 4
    if (highest_paid * 1.5) <= remainder:
        x += 1

    # fib
    # 1, 1, 2, 3, 5, 8, 13, 21, 34
    # 1, 2, 4, 7, 12, 20, 33, 54,
    # sum of fibs 1 -> n = fib(n+2) - 1

    # find highest_fib-1 near total_lambs
    # n = sequence # for highest_fib
    n = math.floor((math.log(total_lambs + 1) + math.log(root5)) / (math.log(alpha)))
    fib_check = fib(n)
    # print("highest fib", n, fib_check)
    if fib_check > (total_lambs + 1):
        n -= 1
    else:
        fib_check = fib(n + 1)
        if fib_check <= (total_lambs + 1):
            n += 1
    # find highest paid worker. -> seq - 2
    # compare remainder vs seq-1. must be more to add worker
    remainder = total_lambs - fib(n) + 1
    y = n - 2
    if remainder > fib(n - 1):
        y += 1
    print("x, y", x, y)
    return int(y - x)
