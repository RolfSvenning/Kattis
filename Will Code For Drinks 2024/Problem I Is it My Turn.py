from functools import cache

n, c = map(int, input().split())

@cache
def f(p, i):
    if p == 0: return 2 * (i == n - 1)
    R = [f(p - j, (i + j + 1) % n) for j in range(1, min(p + 1, n)) if i + j + 1 != n - 1 or p - j == 0]
    if sum(R) == 0: return 0
    return 1 if sum(R) < 2 * len(R) else 2


match f(c, 0):
    case 0: print("no")
    case 1: print("maybe")
    case 2: print("yes")