from __future__ import print_function
n = int(raw_input())
for i in range(n):
    for d in range(i):
        print(end=' ')
    for j in range(2*n-2*i-1):
        print("*", end='')
    print()
