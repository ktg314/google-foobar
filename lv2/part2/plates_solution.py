# input: list from 1 - 9 digits
# each digit 0-9

# find combinations that add up to numbers divisible by 3
# prioritize more digits than highest numbers. ex: 100 > 99
# then just sort from largest number to smallest
def list_to_plate(l):
    if len(l) == 0:
        return 0
    l.sort()
    l.reverse()
    try:
        ret = (''.join(map(str,l)))  # map str turns all items in l to str then combines
    except ValueError:
        pass
    return int(ret)


# list.sort() -> smallest to biggest
# sum(list) => returns int
def answer(l):
    if sum(l) % 3 == 0:
        return list_to_plate(l)
    final_list = [x for x in l if x % 3 == 0]
    remainder_one = [x for x in l if x % 3 == 1]
    remainder_two = [x for x in l if x % 3 == 2]
    sum_rest = sum(remainder_one + remainder_two)
    if sum_rest % 3 == 1:
        if len(remainder_one) > 0:
            remainder_one.sort()
            final_list += remainder_one[1:] + remainder_two
        elif len(remainder_two) > 1:
            remainder_two.sort()
            final_list += remainder_two[2:] + remainder_one
    elif sum_rest % 3 == 2:
        if len(remainder_two) > 0:
            remainder_two.sort()
            final_list += remainder_two[1:] + remainder_one
        elif len(remainder_one) > 1:
            remainder_one.sort()
            final_list += remainder_one[2:] + remainder_two
    return list_to_plate(final_list)
