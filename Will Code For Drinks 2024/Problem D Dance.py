# Solution: maintain the two sequences sorted and always pair A_i with B_i
# If there is a crossing then there is a pair (A_1 - B_2) and (A_2 - B_1) such that A_1 < A_2 and B_1 < B_2,
# then pairs (A_1 - B_1) and (A_2 - B_2) have smaller max difference (and sum of differences actually).
# Implies that all matchings with a crossing are no better than the sorted pairing (since one can move from 
# the matching with crossing to the the sorted one using flips which preserve or decrease the cost)

# Naive solution (with counting sort since heights are k<= 250) run in O((n + k)n) time. 
# Speed up by keeping two arrays A (and similarly B) of size k with A_i = #people_of_height_i. 
# Then compute difference by a merge-like procedure of A and B (or find pair of smallest and largest in 
# each bucket from A to B)

n = int(input())

A =  [0] * (251)
B =  [0] * (251)
Ca = [0] * (251)
Cb = [0] * (251)

for i in range(n):
    #print("round i: ", )
    a, b = list(map(int, input().split()))
    A[a] += 1
    B[b] += 1

    for j in range(50, 250):
        Ca[j] = Ca[j - 1] + A[j]
        Cb[j] = Cb[j - 1] + B[j]

    d = 0
    b = 50  
    for j in range(50, 251):
        if Ca[j] == Ca[j - 1]: continue
        while(Cb[b] < Ca[j - 1] + 1):
            #print(b, Cb[b], Ca[j - 1] + 1)
            b = b + 1
        d = max(d, abs(j - b))
        if Ca[j] - Ca[j - 1] > 1:
            while(Cb[b] < Ca[j]):
                b = b + 1
            d = max(d, abs(j - b))
        if Ca[j] == (i + 1): break

    print(d)

