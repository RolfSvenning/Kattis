# https://wcfd24.kattis.com/contests/wcfd24/problems/aligningbottles
from functools import cache
from collections import deque


# I = int("".join(map(lambda xs: "".join([str(1) if x == "o" else str(0) for x in xs]), [input() for _ in range(4)])), 2)

I = int("0b010101100101001000110011", 2) # sample 3
B = I.bit_count()
print("\n".join("".join(["o" if x == "1" else "." for x in format(I, "024b")[6 * i: 6 * (i + 1)]]) for i in range(4)))

def Ns(s):
    for ds in [-1 if s not in [0, 6, 12, 18] else 25, 1 if s not in [5, 11, 17, 23] else 25, -6, 6]:
        if 0 <= s + ds < 24: yield s + ds

def BFS(S):
    S_bin = format(S, "024b")

    Q = deque([min([i for i in range(24) if S_bin[i] == "1"])])
    V = set()
    while Q:
        s = Q.popleft()
        if s in V: continue
        V.add(s)
        for q in Ns(s):
            if S_bin[q] != "0": Q.append(q)
            
    return S, len(V) == B


@cache
def f(S, M):
    if M == 0: return BFS(S)
    
    S_bin = format(S, "024b")
    for i in range(24):
        for j in range(i + 1, 24):
            if not int(S_bin[-(i + 1)]) or int(S_bin[-(j + 1)]): continue # invalid move
            res, Possible = f((S & ((1 << i) ^ ((1 << 24) - 1))) | (1 << j), M - 1) # make move
            if Possible: return res, True
    return None, False

for i in range(24):
    S, Pos = f(I, i)
    if Pos: 
        print(i, S, format(S, "024b"))
        print("\n".join("".join(["o" if x == "1" else "." for x in format(S, "024b")[6 * i: 6 * (i + 1)]]) for i in range(4)))
        break

