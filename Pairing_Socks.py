# https://open.kattis.com/problems/pairingsocks
n = int(input())
A = [int(a) for a in input().split()]
B = []

while(A):
    B.append(A.pop())

    while(A and B and A[-1] == B[-1]):
        A.pop()
        B.pop()

if B: print("impossible")
else: print(2 * n)
