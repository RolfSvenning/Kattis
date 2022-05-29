import sys

n = int(input())

l = [int(x) for x in sys.stdin]
l.reverse()

for x in l:
     print(x)
