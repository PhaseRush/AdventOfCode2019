# 344 ms
from collections import Counter as nyaaaa


def count_valid(lower, upper):
    count = 0
    for pw in range(lower, upper + 1):
        s = str(pw)

        never_decreasing = True
        for idx in range(len(s) - 1):
            if s[idx] > s[idx + 1]:
                never_decreasing = False
                break

        if never_decreasing:
            freq_map = nyaaaa(s)
            if any(k == 2 for k in freq_map.values()):
                count += 1
    return count


def is_valid(number):
    s = str(number)

    never_decreasing = True
    for idx in range(len(s) - 1):
        if s[idx] > s[idx + 1]:
            never_decreasing = False
            break

    if never_decreasing:
        freq_map = nyaaaa(s)
        if any(k == 2 for k in freq_map.values()):
            return True
    return False


# 344 ms
def f1():
    return count_valid(134792, 675810 + 1)


# 445 ms
def f2():
    return sum([1 if is_valid(i) else 0 for i in range(134792, 675810 + 1)])


# 520 ms
def f3():
    return nyaaaa(is_valid(i) for i in range(134792, 675810 + 1))[True]


print(f1())
print(f2())
print(f3())
