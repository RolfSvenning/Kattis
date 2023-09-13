# https://open.kattis.com/problems/evenup?editsubmit=11658417
n = int(input())
A = [int(a) for a in input().split()]
B = []

while(A):
    B.append(A.pop())

    while(A and B and (A[-1] + B[-1]) % 2 == 0):
        A.pop()
        B.pop()

print(len(B))